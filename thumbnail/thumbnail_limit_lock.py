#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/8/23 0:12
# @Author  : Xuhaozhang
# @Email   : xuhaozhang_hfut@163.com
# @File    : thumbnail_limit_lock.py
from __future__ import print_function

import threading
import time
import string
import random
import urllib2
import Queue
import sys

import uuid
from PIL import Image


HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
           'AppleWebKit/537.36 (KHTML, like Gecko) '
           'Chrome/92.0.4515.131 Safari/537.36 Edg/92.0.902.67'}


class ThumbnailURL_Generator(threading.Thread):
    """ Worker class that generates images URLs """

    def __init__(self, queue, sleep_time=1,):
        self.sleep_time = sleep_time
        self.queue = queue
        # A flag for stopping
        self.flag = True
        # choice of sizes
        self.sizes = (240, 320, 360, 480, 600, 720)
        # URL scheme
        self.url_template = 'https://dummyimage.com/%s/%s/%s.jpg'
        threading.Thread.__init__(self, name='producer')

    def __str__(self):
        return 'Producer'

    def get_size(self):
        return '%dx%d' % (random.choice(self.sizes), random.choice(self.sizes))

    def get_color(self):
        return ''.join(random.sample(string.hexdigits[:-6], 3))

    def run(self):
        """ Main thread function """

        while self.flag:
            # generate image URLs of random sizes and flag fg/bg colors
            url = self.url_template % (
                self.get_size(), self.get_color(), self.get_color())
            # Add to queue
            print(self, 'put', url)
            self.queue.put(url)
            time.sleep(self.sleep_time)

    def stop(self):
        """ Stop the thread """
        self.flag = False


class ThumbnailImageSaver(object):
    """ class which save URLs to thumbnail images and keeps a counter """

    def __init__(self, limit=10):
        self.limit = limit
        self.lock = threading.Lock()
        self.counter = {}

    def thumbnail_image(self, url, size=(64, 64), format='.png'):
        """ Save thumbnail of an image URL """

        req = urllib2.Request(url=url, headers=HEADERS)
        im = Image.open(urllib2.urlopen(req))
        # filename is last part of the URL minus extension + '.format'
        filename = url.split('/')[-1].split('.')[0] + '_thumb' + format
        im.thumbnail(size, Image.ANTIALIAS)
        im.save(filename)
        print('Saved', filename)
        self.counter[filename] = 1
        return True

    def save(self, url):
        """ Save a url thumbnail """

        with self.lock:
            if len(self.counter) >= self.limit:
                return False
            self.thumbnail_image(url)
            print('\tCount=>', len(self.counter))
            return True


class ThumbnailURL_Consumer(threading.Thread):
    """ Worker class that consumes URLs and generates thumbnails """

    def __init__(self, queue, saver):
        self.queue = queue
        self.flag = True
        self.saver = saver
        # internal ID
        self.id = uuid.uuid4().hex
        threading.Thread.__init__(self, name='Consumer-' + self.id)

    def __str__(self):
        return 'Consumer-' + self.id

    def run(self):
        """ Main thread function """

        while self.flag:
            url = self.queue.get()
            print(self, 'Got', url)
            if not self.saver.save(url):
                # Limit reached, break out
                print(self, 'Set limit reached, quitting')
                break

    def stop(self):
        """ Stop the thread """

        self.flag = False


if __name__ == "__main__":
    import glob
    import os

    os.system('rm -f *.png')
    q = Queue.Queue(maxsize=2000)
    saver = ThumbnailImageSaver(limit=50)

    producers, consumers = [], []
    for i in range(3):
        t = ThumbnailURL_Generator(q)
        producers.append(t)
        t.start()

    for i in range(5):
        t = ThumbnailURL_Consumer(q, saver)
        consumers.append(t)
        t.start()

    for t in consumers:
        t.join()
        print('Joined', t)
        sys.stdout.flush()

    # To make sure producers dont block on a full queue
    while not q.empty():
        item = q.get()

    for t in producers:
        t.stop()
        print('Stopped', t)
        sys.stdout.flush()

    print('Total number of PNG images', len(glob.glob('*.png')))

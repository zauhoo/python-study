#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/8/21 20:28
# @Author  : Xuhaozhang
# @Email   : xuhaozhang_hfut@163.com
# @File    : thumbnail_pc.py

import threading
import time
import string
import random
import urllib2
import Queue

from PIL import Image


HEADERS = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
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
        return '%dx%d' % (random.choice(self.sizes),random.choice(self.sizes))

    def get_color(self):
        return ''.join(random.sample(string.hexdigits[:-6], 3))

    def run(self):
        """ Main thread function """

        while self.flag:
            # generate image URLs of random sizes and flag fg/bg colors
            url = self.url_template % (self.get_size(),
                                       self.get_color(),
                                       self.get_color())
            # Add to queue
            print self, 'put', url
            self.queue.put(url)
            time.sleep(self.sleep_time)

    def stop(self):
        """ Stop the thread """
        self.flag = False


class ThumbnailURL_Consumer(threading.Thread):
    """ Worker class that consumes URLs and generates thumbnails """

    def __init__(self, queue):
        self.queue = queue
        self.flag = True
        threading.Thread.__init__(self, name='consumer')

    def __str__(self):
        return 'Consumer'

    def thumbnail_image(self, url, size=(64,64), format='.png'):
        """ Save thumbnail of an image URL """

        req = urllib2.Request(url=url, headers=HEADERS)
        im = Image.open(urllib2.urlopen(req))
        # filename is last part of the URL minus extension + '.format'
        filename = url.split('/')[-1].split('.')[0] + '_thumb' + format
        im.thumbnail(size, Image.ANTIALIAS)
        im.save(filename)
        print self, 'Saved', filename

    def run(self):
        """ Main thread function"""

        while self.flag:
            url = self.queue.get()
            print self, 'Got', url
            self.thumbnail_image(url)

    def stop(self):
        """ Stop the thread """

        self.flag = False


if __name__ == "__main__":

    q = Queue.Queue(maxsize=200)
    producers, consumers = [], []

    for i in range(2):
        t = ThumbnailURL_Generator(q)
        producers.append(t)
        t.start()

    for i in range(2):
        t = ThumbnailURL_Consumer(q)
        consumers.append(t)
        t.start()


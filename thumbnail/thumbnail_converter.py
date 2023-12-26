#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/8/15 16:47
# @Author  : Xuhaozhang
# @Email   : xuhaozhang_hfut@163.com
# @File    : mysql_conn.py

from PIL import Image
import urllib2
import time
import threading

HEADERS = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 Edg/92.0.902.67'}

def thumbnail_image(url, size=(64, 64), format='.png'):
    """ Save thumbnail of an image URL """

    req = urllib2.Request(url=url, headers=HEADERS)
    im = Image.open(urllib2.urlopen(req))
    # filename is last part of the URL minus extension + '.format'
    pieces = url.split('/')
    filename = ''.join((pieces[-2],'_',pieces[-1].split('.')[0],'_'
                                                                'thumb',format))
    im.thumbnail(size, Image.ANTIALIAS)
    im.save(filename)
    print 'Saved',filename


if __name__=='__main__':
    img_urls = [
        'https://dummyimage.com/256x256/000/fff.jpg',
        'https://dummyimage.com/320x240/fff/00.jpg',
        'https://dummyimage.com/640x480/ccc/aaa.jpg',
        'https://dummyimage.com/128x128/ddd/eee.jpg',
        'https://dummyimage.com/720x720/111/222.jpg'
    ]
    start = time.clock()
    for url in img_urls:
        t = threading.Thread(target=thumbnail_image, args=(url,))
        t.start()
        # thumbnail_image(url)
    end = time.clock()
    print 'Running time: %s Seconds' % (end - start)

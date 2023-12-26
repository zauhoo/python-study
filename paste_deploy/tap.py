#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/7/2 16:17
# @Author  : Xuhaozhang
# @Email   : xuhaozhang_hfut@163.com
# @File    : tap.py

class Tap(object):

    def __init__(self, in_arg):
        self.in_arg = in_arg

    def __call__(self, environ, start_response):
        print('Tap')
        start_response('200 OK', [('Content Type', 'test/plain')])
        return ['%s, %s!n' % (self.in_arg, 'Tap') ]


def app_factory(global_config, in_arg):
    return Tap(in_arg)
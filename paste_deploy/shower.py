#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/7/2 22:10
# @Author  : Xuhaozhang
# @Email   : xuhaozhang_hfut@163.com
# @File    : shower.py

class Shower(object):

    def __init__(self, in_arg):
        self.in_arg = in_arg

    def __call__(self, environ, start_response):
        print('Shower')
        start_response('200 OK', [('Content Type', 'test/plain')])
        return ['%s, %s!n' % (self.in_arg, 'Shower')]


def app_factory(global_config, in_arg):
    return Shower(in_arg)
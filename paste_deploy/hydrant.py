#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/7/5 23:30
# @Author  : Xuhaozhang
# @Email   : xuhaozhang_hfut@163.com
# @File    : hydrant.py

class Hydrant(object):

    def __init__(self, in_arg):
        self.in_arg = in_arg

    def __call__(self, environ, start_response):
        print('Hydrant')
        start_response('200 OK', [('Content Type', 'test/plain')])
        return ['%s, %s!n' % (self.in_arg, 'Hydrant')]


def app_factory(global_config, in_arg):
    return Hydrant(in_arg)

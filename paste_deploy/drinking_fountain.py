#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/7/6 0:34
# @Author  : Xuhaozhang
# @Email   : xuhaozhang_hfut@163.com
# @File    : drinking_fountain.py

class DrinkingFountain(object):
    def __init__(self, in_arg):
        self.in_arg = in_arg

    def __call__(self, environ, start_response):
        print('DrinkingFountain')
        start_response('200 ok', [('Content Type', 'text/plain')])
        return ['%s, %s!\n' % (self.in_arg, 'DrinkingFountain')]


def app_factory(global_config, in_arg):
    return DrinkingFountain(in_arg)
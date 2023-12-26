#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/7/6 0:47
# @Author  : Xuhaozhang
# @Email   : xuhaozhang_hfut@163.com
# @File    : purifier.py

class Purifier(object):
    def __init__(self, app, in_arg):
        self.app = app
        self.in_arg = in_arg

    def __call__(self, environ, start_response):
        print('Purifier')
        return self.app(environ, start_response)


def filter_app_factory(app, global_config, in_arg):
    return Purifier(app, in_arg)
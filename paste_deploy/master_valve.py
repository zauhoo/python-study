#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/7/2 16:12
# @Author  : Xuhaozhang
# @Email   : xuhaozhang_hfut@163.com
# @File    : master_valve.py

import os

from wsgiref.simple_server import make_server
from paste import httpserver
from paste.deploy import loadapp

if __name__ == '__main__':
    configfile = 'configure.ini'
    appname = 'main'
    wsgi_app = loadapp('config:%s' % os.path.abspath(configfile), appname)

    # httpserver.serve(loadapp('config:configure.ini', relative_to = '.'), host = '127.0.0.1', port=8000)

    server = make_server('localhost', 8000, wsgi_app)
    server.serve_forever()

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/6/11 14:29
# @Author  : Xuhaozhang
# @Email   : xuhaozhang_hfut@163.com
# @File    : myapp.py

import time
from flask import Flask
import threading
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

@app.route('/')
def hello_world():
    id = threading.currentThread().ident
    return 'Hello World! Thread is %s' % id

@app.route("/index")
def index_test():
    print("index test,sleep for 15 second")
    time.sleep(15)
    return "index test for non-block"

@app.route("/sum")
def sum():
    t1 = time.time()
    for i in range(100000000):
        result = 100 - i
    id = threading.currentThread().ident
    return "thread is %s, sum is %s ,time is %s" % (id, result, time.time() - t1)

@app.route("/sum1")
def sum1():
    t1 = time.time()
    for i in range(100000000):
        result = 100 - i
    id = threading.currentThread().ident
    return "thread is %s, sum is %s ,time is %s" % (id, result, time.time() - t1)


if __name__ == '__main__':
    print(__name__)
    app.run(host="192.168.32.128", port=8088, debug=True)


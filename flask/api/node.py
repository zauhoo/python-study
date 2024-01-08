#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/1/9 0:07
# @Author  : Xuhaozhang
# @Email   : xuhaozhang_hfut@163.com
# @File    : node.py

from flask_restful import Resource


class Node(Resource):
    """

    """

    @staticmethod
    def get():
        import requests
        requests.get("http://www.baidu.com")
        return "Google says hello!"

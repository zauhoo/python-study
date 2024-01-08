#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/1/9 1:01
# @Author  : Xuhaozhang
# @Email   : xuhaozhang_hfut@163.com
# @File    : __init__.py

from flask import Blueprint
from flask_restful import Api

from node import Node


api_bp = Blueprint("/api/v1", __name__)
api = Api(api_bp)

api.add_resource(Node, "/node/info")
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/1/9 0:07
# @Author  : Xuhaozhang
# @Email   : xuhaozhang_hfut@163.com
# @File    : app.py

import importlib

from pyinstrument import Profiler
from flask import Flask, g, make_response, request


class FlaskServer(object):
    """

    """

    def __init__(self, ip=None, port=None, ssl_context=()):
        """"""
        self._ip = ip
        self._port = port
        self._ssl_context = ssl_context
        self._app = Flask(__name__)
        self._app.before_request(self.before_request)
        self._app.after_request(self.after_request)

    def before_request(self):
        if "profile" in request.args:
            g.profiler = Profiler()
            g.profiler.start()

    def after_request(self, response):
        if not hasattr(g, "profiler"):
            return response

        g.profiler.stop()
        output_html = g.profiler.output_html()
        return make_response(output_html)

    def register_api(self):
        bp_ver = "api"
        mod = importlib.import_module(bp_ver)
        self._app.register_blueprint(mod.api_bp)

    def launch(self):
        """ run Flask application"""

        app_args = {
            "host": self._ip,
            "port": self._port,
            "threaded": True
        }

        if self._ssl_context:
            app_args["ssl_context"] = self._ssl_context

        self.register_api()

        self._app.run(**app_args)


if __name__ == '__main__':
    host = "192.168.32.141"
    port = 8080
    ssl_context = ()

    flask_server = FlaskServer(host, port, ssl_context=ssl_context)
    flask_server.launch()

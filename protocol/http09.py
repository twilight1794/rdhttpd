#!/usr/bin/env python3

import importlib
import os

class server(object):
    def serve(self, request):
        '''Here we redefine the server() function'''
        treq = request.partition(" ")
        treq = list(treq)
        treq[2] = treq[2][:-5]
        if treq[0] != "GET":
            return "HTTP/0.9 400 Bad request"
        else:
            try:
                mod = importlib.import_module(treq[2])
                return str(mod.main({}))
            except RuntimeError:
                return "HTTP/0.9 404 Not Found:" + os.path.abspath(treq[2])

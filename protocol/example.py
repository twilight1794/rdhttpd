#!/usr/bin/env python3

import importlib
import os

class Exampleserver(server):
    def server(self, request):
        '''Here we redefine the server() function'''
        return 'HTTP/1.0 200 OK\n\n<html><body><h1>It Works!!!</h1></body></html>'

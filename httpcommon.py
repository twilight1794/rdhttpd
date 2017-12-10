#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Date of version: 9/dic/2017 (G. C.)
# The Rainbow Dash HTTP Daemon Server
# Copyright © 2017 Giovanni Alfredo Garciliano Díaz

# This file is part of rdhttpd
# rdhttpd is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# rdhttpd is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with rdhttpd.  If not, see <http://www.gnu.org/licenses/>.

class httpreq(object):
    '''Base class for any HTTP request'''
    def __init__(self):
        self.rawrequest = ""
        self.headerlines = {
            "requestLine": ""
       }
    def parse(self, req):
        '''Accepts a string containing a raw HTTP request (as sended by the client, but converted to string)
        Returns a dictionary where the key is the header name, and the value is the header value
        The first key is called "requestLine", and contains a tuple with 3 items: method, requested resource, and HTTP version,'''
        self.rawrequest = req
        listrequest = self.rawrequest.splitlines().pop() # Pop the lastline
        i = 1  # Number of Iteration
        for string in listrequest:
            if i == 1:
                self.headerlines.setdefault("requestLine", string)
            else:
                stringtuple = string.split(": ")
                self.headerlines[stringtuple[0]] = stringtuple[1]
            i += 1
        return self.headerlines

class httpresp(object):
    '''Base class for any HTTP response'''
    def __init__(self):
        self.content = ""
        self.header = {
            "statusLine": "",
        }
        self.header["statusLine"] = "HTTP 1.0 200 OK"
    def setHeader(self, headern, value):
        self.header.setdefault(headern, value)
        return str(headern) + str(value)
    def rmHeader(self, headern):
        del(self.header[headern])
        return str(headern)
    def __str__(self):
        string = ""
        i = 1
        for key, value in self.header.items():
            if i == 1:
                string += str(value) + "\r\n"
            else:
                string += str(key) + str(value) + "\r\n"
            i += 1
        string += "\r\n"
        string += self.content
        return string

def getFileRequested(filer): # In rev
    '''This function returns the file passed by parameter. First, check the list of available CGIs. If the file requested is on that list, will be execute the CGI and will return the result. Otherwise, will be served the file directly.'''
    if filer in cgilist:
        try:
            importlib.import_module(filer)
        except ImportError:
            raise ImportError("The CGI isn't available")
    else:
        try:
            filerequested = open(filer, "rb")
            return filerequested.read()
        except:
            raise RuntimeError("The file isn't available")
        finally:
            filerequested.close()

class HTTPRespCode(object):
    """A class that manages all related about HTTP status codes"""
    def __init__(self, code):
        try:
            for i in httpconst.statuscodes:
                if str(code) == i[0]:
                    self.code = i[0]
                    self.strcode = i[0] + " " + i[1]
                    break
                else:
                    continue
            len(self.code)
        except AttributeError:
            raise ValueError("The parameter must be an valid HTTP status code")
    def __str__(self):
        return self.strcode

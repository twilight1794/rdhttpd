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

import os
import sys
import re
import glob
import importlib
import socket
import threading

loadedprotoc = []

appInfo = {
    "name": "Rainbow Dash HTTP Daemon",
    "version": "0.1",
    "author": "Giovanni Alfredo Garciliano Diaz",
    "license": "GNU GPLv3",
    "buildDate": "vie 09 jun 2017 09:37:52 CDT",
}

# Creating the superglobals
SERVER = {
    "SERVER_ADDR": "",
}

class server(object):
    ''' Base class for implement the socket'''
    def __init__(self, host, port, timeout, listen, log):
        self.host = host
        self.port = port
        self.timeout = timeout
        self.listen = listen
        self.socketId = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socketId.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.socketId.bind((host, port))
    def start(self):
        self.socketId.listen(self.listen)
        while True:
            client, address = self.socketId.accept()
            client.settimeout(self.timeout)
            threading.Thread(target = self.listenClient,args = (client,address)).start()
    def listenClient(self, client, address):
        recvmsg = client.recv(65355)
        sendmsg = self.server(recvmsg.decode("utf-8"))
        client.send(sendmsg.encode())
        client.close()
    def server(self, request):
        response = "Example"
        return response

def listenClient(client, address):
    recvmsg = client.recv(65355)
    sendmsg = recvmsg.decode("utf-8")
    objmsg = httpcommon.httpreq().parse(sendmsg)
    # select protocol
    for y in config.protocols:
        if re.match(y[1], objmsg["requestLine"]):
            pass
        else:
            continue;
    client.send(sendmsg.encode())
    client.close()

if __name__ == "__main__":
    print(appInfo["name"] + " v" + appInfo["version"])
    print("INFO: Currently executing from " + os.getcwd())
    try:
        import config
    except:
        print("FATAL: Failed to import config.py")
        exit(1)
    else:
        print("DEBUG: Imported config.py")
    try:
        import httpconst
        import httpcommon
    except:
        print("FATAL: Failed to import main libraries")
        exit(1)
    else:
        print("DEBUG: Imported main libraries")
    # Loads the protocol-modules listed on config.protocols
    for nametuple in config.protocols:
        filemod = os.path.join(config.protocolpath, nametuple[0])
        if os.path.isfile(filemod):
            try:
                path, filemod = os.path.split(filemod)
                module = "{0}.{1}".format(path, filemod[:-3])
                print("DEBUG: Importing", module)
                loadedprotoc.append(importlib.import_module(module))
            except OSError as e:
                print("ERROR: Failed to import protocol " + filemod)
                continue
            else:
                print("INFO: Imported " + module)
    # Initialize the servers
    socketId = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socketId.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    try:
        print("DEBUG: Intializing socket...")
        socketId.bind((config.host, config.port))
    except RuntimeError:
        print("FATAL: Failed to create a socket")
        exit(2)
    socketId.listen(config.listen)
    print("INFO: Listening at port " + str(config.port) + "!!!")
    while True:
        client, address = socketId.accept()
        client.settimeout(config.timeout)
        threading.Thread(target = listenClient, args = (client,address)).start()

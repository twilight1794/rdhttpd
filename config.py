#!/usr/bin/env python3
# rdhttpd config
# Do not touch this file unless you know what you are doing

import os
import sys

protocolpath = "protocol/"
protocols = (
    ("http09.py", "GET /?.+"),
    ("example.py", ".*")
)

host = "0.0.0.0"
port = 8080
timeout = 10
listen = 10

# User-agent
o = os.uname()
uadata = {
    "ServerName": "RainbowDash",
    "ServerVersion": "0.1",
    "PlatformName": "Python",
    "PlatformVersion": str(sys.version_info[0]) + "." + str(sys.version_info[1]) + "." + str(sys.version_info[2]), # e.g. 3.4.3
    "OSName": "LinuxMint",
    "OSVersion": "17.3",
    "KernelName": o.sysname, # e.g. Linux
    "KernelVersion": o.release + ", " + o.machine, # e.g. 3.19.0-32-generic, x86_64
}
useragent = uadata["ServerName"] + "/" + uadata["ServerVersion"] + "(" + uadata["PlatformName"] + "/" + uadata["PlatformVersion"] + ") " + uadata["OSName"] + "/" + uadata["OSVersion"] + "(" + uadata["KernelName"] + "/" + uadata["KernelVersion"] + ")" # e.g. 'RainbowDash/1.0(Python/3.4.3) LinuxMint/17.3(Linux/3.19.0-32-generic, x86_64)'

#    ("http10", "(GET|POST|HEAD) /?.+ HTTP/1\.0"),
#    ("http11", "(GET|POST|HEAD|PUT|DELETE|TRACE|OPTIONS|CONNECT) /?.+ HTTP/1\.1"),

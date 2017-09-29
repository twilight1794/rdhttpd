#!/usr/bin/env python3
# -*- coding: utf-8 -*-
HTTP_DIR = "/home/giobeatle1794/git/rainbow-dash/public_html/"
def server(recvmsg):
	filerequested = HTTP_DIR + "index.html"
	print(filerequested)
	myfile = open(filerequested, "r") 
	content = myfile.read()
	return content

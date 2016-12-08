#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from http.server import HTTPServer, BaseHTTPRequestHandler
from os import curdir, sep
import cgi
# HTTPRequestHandler class
class Handler(BaseHTTPRequestHandler):
	# GET
	server_version = "RainbowDash/0.1.pre1"
	def do_GET(self):
		try:
			#Check the file extension required and
			#set the right mime type
			sendReply = False
			if self.path.endswith(".py"):
				mimetype='text/html'
				sendReply = True
			if sendReply == True:
				#Open the static file requested and send it
				f = open(curdir + sep + self.path)
			# Send response status code
			self.send_response(200)
			# Send headers self.send_header('Server','RainbowDash/0.1.pre1 (Python/3.4.3) LinuxMint/17.3(Linux/3.19.0.32;generic;x86_64)')
			self.send_header('Content-type',mimetype)
			self.end_headers()
			# Send message back to client
			message = self.request_version
			# Write content as utf-8 data
			self.wfile.write(bytes(message, "utf8"))
			return
		except IOError:
			self.send_error(404,'File Not Found: %s' % self.path)
'''	def do_POST(self):
		if self.path=="/send":
			form = cgi.FieldStorage(
				fp=self.rfile, 
				headers=self.headers,
				environ={'REQUEST_METHOD':'POST',
		                 'CONTENT_TYPE':self.headers['Content-Type'],
			})
			print "Your name is: %s" % form["your_name"].value
			self.send_response(200)
			self.end_headers()
			self.wfile.write("Thanks %s !" % form["your_name"].value)
			return'''
try:
	print('starting server...')
	# Server settings
	# Choose port 8080, for port 80, which is normally used for a http server, you need root access
	server_address = ('0.0.0.0', 80)
	httpd = HTTPServer(server_address, Handler)
	print('running server...')
	httpd.serve_forever()
except KeyboardInterrupt:
	print (' received, shutting down the web server')
	httpd.socket.close()
#	cgi_directories = ["/"]

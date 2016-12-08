#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import cgi
# Headers
print("Status: 200 OK")
print("Content-Type: text/html")
print("Charset: utf-8")
print("Server: RainbowDash/0.1.pre1 (Python/3.4.3) LinuxMint/17.3(Linux/3.19.0.32;generic;x86_64)")
print("")
# Contenido (texto plano, como lo hemos especificado)
url_input = cgi.FieldStorage()
if "name" not in url_input:
	print("<html>¡No me has dicho tu nombre!</html>")
else:
	print("""
	<html>
	<head>
	<title>Título de la página</title>
	</head>
	<h3>Hola %s!</h3>
	</html>""" % url_input["name"].value)

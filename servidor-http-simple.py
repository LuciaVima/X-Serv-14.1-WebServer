#!/usr/bin/python
#Lucia Villa Martinez
# -*- coding: utf-8 -*-

import socket

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mySocket.bind(('localhost', 1234))
mySocket.listen(5)
while True:
	print 'Waiting for connections'
	(recvSocket, address) = mySocket.accept()
	print 'HTTP request received:'
	print recvSocket.recv(1024)
	recvSocket.send("HTTP/1.1 200 OK\r\n\r\n")
	recvSocket.send("Hola! Eres de esta IP ")
	recvSocket.send(address[0])
	recvSocket.send(" y este puerto ")
	recvSocket.send(str(address[1]))
	recvSocket.send("\r\n")
	recvSocket.close()

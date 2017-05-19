#!/usr/bin/python  
# -*- coding: utf-8 -*- 
#import socket module
from socket import *
import ssl

context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
context.load_cert_chain(certfile="cert.pem")
#creat a server socket
serverSocket = socket(AF_INET, SOCK_STREAM) 

serverPort=30000
serverSocket.bind(('',serverPort))
serverSocket.listen(1)
while True:
#Establish the connection
	print 'Ready to serve...'
	connectionSocket, addr = serverSocket.accept() 
	connstream = context.wrap_socket(connectionSocket, server_side=True)
	try:
		message = connstream.recv(1024)
		filename = message.split()[1]
		f = open(filename[1:])
		#f = open(message)
		outputdata = f.read()
		# Send one HTTP header line into socket 
		header="HTTP/1.0 200 OK\r\nContent-Type: text/html\r\n\r\n"
		connstream.send(header)
		#Send the content of the requested file to the client 
		for i in range(0, len(outputdata)):
			connstream.send(outputdata[i])
		
		connstream.close()
#	except IOError:
	#Send response message for file not found 
	except IOError:
#		f=open('404.html')
#		outputdata=f.read()
#		header="HTTP/1.0 200 OK\r\nContent-Type: text/html\r\n\r\n"
#		connectionSocket.send(header)
#		for i in range(0, len(outputdata)):
#			connectionSocket.send(outputdata[i])
		connstream.send('<html><body><h1>Page not found</body></html>')
		connstream.close()
serverSocket.close()
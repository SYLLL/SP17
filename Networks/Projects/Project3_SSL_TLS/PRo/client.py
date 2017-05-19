#!/usr/bin/python  
# -*- coding: utf-8 -*-  

from socket import *
import time
import sys
import ssl
import pprint

#serverName='127.0.0.1'
#serverPort=30000
#filename=raw_input("Please enter optionals, hostname, portnumber and filename\n(here portnumber is 30000)\n").split()[-1]
filename = sys.argv[-1]
serverPort = int(sys.argv[-2])
serverName = sys.argv[-3]


#1. Instantiating an SSL/TLS context
#2. Setting TLS/SSL client options
#3. Setting the default TLS root certificate paths (e.g., with load_default_certs())
context = ssl.create_default_context()

#context.load_default_certs()

count = 1
for x in sys.argv:
	if x=="--tlsv1.0":
		#ssl_vers=ssl.PROTOCOL_TLSv1
		#context.options |= ssl.OP_NO_TLSv1
		context = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
	elif x=="--tlsv1.1":
		#ssl_vers=ssl.PROTOCOL_TLSv1_1
		#context.options |= ssl.OP_NO_TLSv1_1
		context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_1)
	elif x=="--tlsv1.2":
		#ssl_vers=ssl.PROTOCOL_TLSv1_2
		#context.options |= ssl.OP_NO_TLSv1_2
		context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
	elif x=="--sslv3":
		#ssl_vers=ssl.PROTOCOL_SSLv3
		#context.options |= ssl.OP_NO_SSLv3
		context = ssl.SSLContext(ssl.PROTOCOL_SSLv3)
	elif x=="--ciphers":
		#ciph = sys.argv[count+1]
		context.set_ciphers(sys.argv[count+1])
	elif x=="--cacert":
		#cacert = sys.argv[count+1]
		context.load_cert_chain(sys.argv[count+1])
	count = count + 1

#context.verify_mode = ssl.CERT_NONE

context.verify_mode = ssl.CERT_REQUIRED
context.check_hostname = False
context.load_verify_locations(cafile="cert.pem")
#4. Instantiating a TCP socket
clientSocket=socket(AF_INET, SOCK_STREAM)

#5. Wrapping the TCP socket with the SSL/TLS context
ssl_sock = context.wrap_socket(clientSocket, server_hostname=serverName)
#ssl_sock = context.wrap_socket(clientSocket)

#6. Initiating a connection (to an SSL/TLS server at port 443) and performing an HTTP GET
ssl_sock.connect((serverName, serverPort))


#send msg
#message="GET /%s HTTP/1.1\r\nAccept: text/plain, text/html, text/*\r\n\r\n"%filename

#ssl_sock.send(message)
#time.sleep(1) #handle the Broken Pipe error in the server side
#rev msg
#information=ssl_sock.read(1024)
#print information

#Part 3
cert = ssl_sock.getpeercert()
pprint.pprint(cert)

#7. Closing the socket
ssl_sock.close()

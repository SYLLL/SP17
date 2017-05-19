#import socket module 
import socket, ssl

context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
#context.load_cert_chain(certfile="cert.pem")

serverPort = 13000
serverSocket = socket.socket() #Prepare a sever socket 
serverSocket.bind(('71.206.30.215',serverPort))
serverSocket.listen(1)
print 'The server is ready to receive'
#Fill in start
#Fill in end 
while True:
#Establish the connection
	print 'Ready to serve...' 
	newsocket, fromaddr = serverSocket.accept()
	connstream = ssl.wrap_socket(newsocket, cert_reqs=ssl.CERT_NONE, certfile="cacert.pem", keyfile="private.pem", server_side=True)
	#connectionSocket, addr =  serverSocket.accept()
	try:
		message = connstream.recv(1024)
		#message = connstream.read()
		#print(message)
		filename = message.split()[1] 
		print 'filename:'
		print(filename)
		f = open(filename[1:]) 
		outputdata = f.read() 
		connstream.send('HTTP/1.1 200 OK\r\n\r\n')  
		#Send the content of the requested file to the client 
		for i in range(0, len(outputdata)):
			print(outputdata[i])
			connstream.send(outputdata[i]) 
		connstream.send('end')
		connstream.close()
		print "finish sending"
	except IOError:
		print('ERRORRRR')
		connstream.send('404 Not Found')
		#connstream.write('404 Not Found')
		connstream.close()


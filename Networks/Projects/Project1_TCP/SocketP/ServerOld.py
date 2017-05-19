#import socket module 
from socket import * 
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM) #Prepare a sever socket 
serverSocket.bind(('',serverPort))
serverSocket.listen(1)
print 'The server is ready to receive'
#Fill in start
  #Fill in end 
while True:
#Establish the connection
	print 'Ready to serve...' 
	connectionSocket, addr =  serverSocket.accept()
	try:
		message = connectionSocket.recv(1024)
		filename = message.split()[1] 
		print 'filename:'
		print(filename)
		f = open(filename[1:]) 
		outputdata = f.read() 
		connectionSocket.send('HTTP/1.1 200 OK\r\n\r\n')  
		#Send the content of the requested file to the client 
		for i in range(0, len(outputdata)):
			print(outputdata[i])
			connectionSocket.send(outputdata[i]) 
		connectionSocket.close()
	except IOError:
		#Send response message for file not found #Fill in start
		#Fill in end 
		#Close client socket
		#Fill in start
		#Fill in end
		print('ERRORRRR')
		connectionSocket.send('404 Not Found')
		connectionSocket.close()
serverSocket.close()
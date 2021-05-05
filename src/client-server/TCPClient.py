from socket import *

portNum = 42069

serverName = 'localhost'

clientSocket = socket(AF_INET, SOCK_STREAM)

clientSocket.connect((serverName, portNum))

inData = input('Input: ')

clientSocket.send(inData.encode())

res = clientSocket.recv(1024).decode()

print('Echo: ', res)

clientSocket.close()

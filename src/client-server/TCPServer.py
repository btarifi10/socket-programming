from socket import *

portNum = 42069

serverSocket = socket(AF_INET, SOCK_STREAM)

serverSocket.bind(('', portNum))

serverSocket.listen(1)

print('Server Online')

open = True

while open:
    connectedSocket, address = serverSocket.accept()
    req = connectedSocket.recv(1024).decode()
    connectedSocket.send(req.encode())
    open = False
    connectedSocket.close()


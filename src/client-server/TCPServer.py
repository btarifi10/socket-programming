from socket import *

portNum = 42069

serverSocket = socket(AF_INET, SOCK_STREAM)

serverSocket.bind(('', portNum))

serverSocket.listen()

print('Server Online')

online = True

stopCodes = ["EXIT", "exit", "STOP", "stop"]

while online:
    connectedSocket, address = serverSocket.accept()
    connectionOpen = True
    while connectionOpen:
        req = connectedSocket.recv(1024).decode()
        if not req:
            break
        if stopCodes.count(req) == 0:
            connectedSocket.sendall(req.encode())
        else:
            connectedSocket.close()
            connectionOpen = False
        if req == "quit":
            connectedSocket.close()
            serverSocket.close()
            online = False
            connectionOpen = False



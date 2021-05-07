from socket import *

portNum = 42069

serverSocket = socket(AF_INET, SOCK_DGRAM)

serverSocket.bind(('', portNum))

print('Server Online')

online = True

while online:
    req, address = serverSocket.recvfrom(1024)
    if not req:
        break
    serverSocket.sendto(req, address)
    if req == "quit":
        serverSocket.close()
        online = False



from socket import *

# Setting up server address details
portNum = 42070
serverName = gethostbyname(gethostname())
addr = (serverName, portNum)

# Communication standards
bufferSize = 1024
format = 'utf-8'

serverSocket = socket(AF_INET, SOCK_DGRAM)

serverSocket.bind(addr)


def handleRequestUDP(message, address):
    print(f"[{address}] {message.decode(format)}")
    serverSocket.sendto(message, address)


print('[ONLINE] UDP Server is online...')

online = True

while online:
    message, address = serverSocket.recvfrom(bufferSize)
    if not message:
        break
    handleRequestUDP(message, address)



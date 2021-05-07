from socket import *

import threading

def serverThread(req, address, threadId):
    print(req.decode() + "on server thread", threadId)
    serverSocket.sendto(req, address)

portNum = 42069

serverSocket = socket(AF_INET, SOCK_DGRAM)

serverSocket.bind(('', portNum))

print('Server Online')

threadsRunning = []
addresses = []

while True:
    req, address = serverSocket.recvfrom(1024)
    if addresses.count(address) == 0:
        addresses.append(address)
    if not req:
        break
    threadId = addresses.index(address)
    th = threading.Thread(target=serverThread, args=(req, address, threadId))
    th.start()
    threadsRunning.append(th)

    



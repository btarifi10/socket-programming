from socket import *
import threading

def serverThread(connectedSocket, threadId, stopCodes):
    connectionOpen = True
    while connectionOpen:
        req = connectedSocket.recv(1024).decode()
        print(req + "from thread", threadId)
        if not req:
            break
        if stopCodes.count(req) == 0:
            connectedSocket.sendall(req.encode())
        else:
            connectedSocket.close()
            connectionOpen = False

portNum = 42069

serverSocket = socket(AF_INET, SOCK_STREAM)

serverSocket.bind(('', portNum))

serverSocket.listen()

print('Server Online')

online = True

stopCodes = ["EXIT", "exit", "STOP", "stop"]

threadsRunning = []

while online:
    connectedSocket, address = serverSocket.accept()
    threadId = len(threadsRunning)
    th = threading.Thread(target=serverThread, args=(connectedSocket, threadId, stopCodes))
    th.start()
    threadsRunning.append(th)




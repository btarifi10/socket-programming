from socket import *

portNum = 42069

serverName = 'localhost'

clientSocket = socket(AF_INET, SOCK_DGRAM)

stopCodes = ["EXIT", "exit", "STOP", "stop"]
open = True

bufferSize = 1024

while open:
    inData = input('Input: ')
    if inData == "":
        continue
    if stopCodes.count(inData) > 0 or inData == "quit":
        inData = clientSocket.sendto(inData.encode(), (serverName, portNum))
        clientSocket.close()
        open = False
        break
    
    print("")

    while inData:
        numBytesSent = clientSocket.sendto(inData[:bufferSize].encode(), (serverName, portNum))
        inData = inData[numBytesSent:]
        res = clientSocket.recv(bufferSize).decode()
        print('Echo from server: ', res)
    
    print("-------------------------------")
    


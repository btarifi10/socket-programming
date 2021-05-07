from socket import *

portNum = 42069

serverName = 'localhost'

clientSocket = socket(AF_INET, SOCK_STREAM)

clientSocket.connect((serverName, portNum))

stopCodes = ["EXIT", "exit", "STOP", "stop"]
open = True

while open:
    inData = input('Input: ')
    if inData == "":
        continue
    
    print("")
    amtReceived = 0
    amtExp = len(inData)

    clientSocket.sendall(inData.encode())
    if stopCodes.count(inData) > 0 or inData == "quit":
        clientSocket.close()
        open = False
        break
    
    while amtReceived < amtExp:
        res = clientSocket.recv(1024).decode()
        print('Echo from server: ', res)
        amtReceived += len(res)
    
    print("-------------------------------")
    


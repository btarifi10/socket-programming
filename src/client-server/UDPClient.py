from socket import *

# Setting up server address details
portNum = 42070
serverName = gethostbyname(gethostname())
addr = (serverName, portNum)

# Communication standards
bufferSize = 1024
format = 'utf-8'

exitMsg = "EXIT"

# Create UDP socket
clientSocket = socket(AF_INET, SOCK_DGRAM)

def sendMessageUDP(message):
    while message:
        bytesSent = clientSocket.sendto(message[:bufferSize].encode(format), addr)
        message = message[bytesSent:]
        response = clientSocket.recv(bufferSize).decode(format)
        print('Echo from server: ', response)
    
    print("-------------------------------")

while True:
    message = input('Input: ')
    if message == "":
        continue
    if message == exitMsg:
        break
    sendMessageUDP(message)
    


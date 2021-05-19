from socket import *

# Setting up server address details
portNum = 42069
serverName = gethostbyname(gethostname())
addr = (serverName, portNum)

# Communication standards
bufferSize = 1024
disconnectMsg = "SHEESH!"
format = 'utf-8'

# Create socket
clientSocket = socket(AF_INET, SOCK_STREAM)
# Connect to address via socket
clientSocket.connect(addr)

# Function to handle message sending and receiving
def sendMessage(message):
    msg = message.encode(format)
    clientSocket.sendall(message.encode(format))
    if message == disconnectMsg:
        return
    bytesReceived = 0
    bytesExpected = len(message)
    while bytesReceived < bytesExpected:
        response = clientSocket.recv(bufferSize).decode(format)
        print('Echo from server: ', response)
        bytesReceived += len(response)
    print("-------------------------------")

# Initially, socket is open
open = True
while open:
    message = input('Input: ')
    if message == "":
        continue
    
    # Always send message
    # Close immediately if disconnect
    sendMessage(message)
    if message == disconnectMsg:
        clientSocket.close()
        open = False
        break
    

    


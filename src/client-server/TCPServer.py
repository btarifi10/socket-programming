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
serverSocket = socket(AF_INET, SOCK_STREAM)

# Bind to address and listen 
serverSocket.bind(addr)
serverSocket.listen()

def handleClient(conn, addr):
    print(f"[CONNECTED] {addr}")
    connectionOpen = True
    while connectionOpen:
        message = connectedSocket.recv(bufferSize).decode(format)
        if not message:
            break
        if message == disconnectMsg:
            connectionOpen = False
            print(f"[DISCONNECTED] {addr}")
        else:
            print(f"[{addr}] {message}")
            connectedSocket.sendall(message.encode(format))

online = True
print(f'[ONLINE] Server is listening on {serverName}, port {portNum}...')     

while online:
    connectedSocket, address = serverSocket.accept()
    handleClient(connectedSocket, address)



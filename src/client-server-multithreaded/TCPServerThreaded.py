from socket import *
import threading
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
    print(f"[CONNECTED] {addr} on {threading.current_thread().getName()}")
    print(f"[ACTIVE CLIENTS] {threading.active_count() - 1}")
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
print(f'[ONLINE] Server is listening on {serverName}:{portNum}...')     

while online:
    connectedSocket, address = serverSocket.accept()
    tcpRunner = threading.Thread(target=handleClient, args=(connectedSocket, address))
    tcpRunner.start()



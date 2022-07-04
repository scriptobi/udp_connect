import socket

localIP = "127.0.0.1"
localPort = 32768
bufferSize = 1024
msg2Client = "Message to UDP Client"
bytesMsg = str.encode(msg2Client)

# create datagram socket
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# bind to address and ip
serverSocket.bind((localIP, localPort))
print("UDP server is up and listening")

# listening for incoming messages
while(True):
    bytesObj = serverSocket.recvfrom(bufferSize)
    msg = bytesObj[0]
    adr = bytesObj[1]
    clientMsg = "Message from client:{}".format(msg)
    clientAdr = "Client IP Address: {}".format(adr)
    print(clientMsg)
    print(clientAdr)

    # Sending reply to client
    serverSocket.sendto(bytesMsg, adr)
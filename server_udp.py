import socket

# localIP = "192.168.0.34"
hostname = socket.gethostname()
localIP = socket.gethostbyname(hostname)
localPort = 5000
bufferSize = 1024
msg2Client = "Hello Client !"
bytesMsg = str.encode(msg2Client)

# create datagram socket
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# bind to address and ip
serverSocket.bind((localIP, localPort))
cnxMsg = "UDP server is up and listening on {}.".format(localIP)
print(cnxMsg)

# listening for incoming messages
while True:
    bytesObj = serverSocket.recvfrom(bufferSize)
    msg = bytesObj[0]
    adr = bytesObj[1]
    clientMsg = "Message du client:{}".format(msg)
    clientAdr = "Adresse IP du client: {}".format(adr)
    print(clientMsg)
    print(clientAdr)

    # Sending reply to client
    serverSocket.sendto(bytesMsg, adr)

import socket

localIP = "127.0.0.1"
localPort = 32768
bufferSize = 1024
msg2Client = "Message to UDP Client"

# create datagram socket
UDPServerSocket = socket.socket(socket.AF_INET, type = socket.SOCK_DGRAM)

# Bind to adress and ip
UDPServerSocket.bind(localIP, localPort)
print("UDP server up")

while(True):
    bytesAdressPair = UDPServerSocket.recvfrom(bufferSize)
    msg = bytesAdressPair[0]
    adr = bytesAdressPair[1]
    clientMsg = "Msg from client: {}".format(msg)
    clientIP = "CLient IP Adr:{}".format(adr)

    print(clientMsg)
    print(clientIP)

    UDPServerSocket.sendto(str.encode(msg2Client), adr)
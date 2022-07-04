import socket

serverAdrPort = ("127.0.0.1", 32768)
msg2Server = "A message from client"
toSend = str.encode(msg2Server)
bufferSize = 1024

# create UDP socket
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# send to server
clientSocket.sendto(toSend, serverAdrPort)
msgFromServer = clientSocket.recvfrom(bufferSize)
msg = "Message from Server {}".format(msgFromServer[0])
print(msg)
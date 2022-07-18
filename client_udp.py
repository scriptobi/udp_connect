import socket

serverIP = input("Adresse IP du server: ")
serverPort = 5000
server = (serverIP, serverPort)
hostname = socket.gethostname()
localIP = socket.gethostbyname(hostname)
msg2Server = "A message from client: "
toSend = str.encode(msg2Server)
bufferSize = 1024

# create UDP socket
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    kb_entry = input("Message: ")
    if not kb_entry:
        toSend = str.encode("Deconnection du client " + localIP)
        clientSocket.sendto(toSend, server)
        break
    else:
        toSend = str.encode(kb_entry)
        # send to server
        clientSocket.sendto(toSend, server)
        msgFromServer = clientSocket.recvfrom(bufferSize)
        msg = "Message from Server {}".format(msgFromServer[0])
        print(msg)

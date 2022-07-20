import socket

hostname = socket.gethostname()
localIP = socket.gethostbyname(hostname)
localPort = 6000

# create socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# bind to address and ip
server.bind((localIP, localPort))
server.listen(1)
print(f'TCP server is up and listening on {localIP}.')

# listening for incomming client
client, clientAddr = server.accept()
print(f'Connection : {clientAddr}')
client.send(str.encode('You are connected to the server.'))
cnx = True
while cnx:
    data = client.recv(1024)
    print(data)
    if not data:
        cnx = False

client.close()
server.close()

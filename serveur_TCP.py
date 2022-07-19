import socket

hostname = socket.gethostname()
localIP = socket.gethostbyname(hostname)
localPort = 6000

# create socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# bind to address and ip
server.bind((localIP, localPort))
print(f'TCP server is up and listening on {localIP}.')

# listening for incomming client
client, clientAddr = server.accept()
print(f'Connection : {clientAddr}')
server.send(str.encode('You are connected to the server.'))

while True:
    data = server.recv(1024)
    print(data)
    #msg = data.decode(data)

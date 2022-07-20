import socket

serverIP = input("Adresse IP du server: ")
serverPort = 6000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.connect((serverIP, serverPort))
print(f'Connection to {serverIP}:{serverPort} done.')
serverMsg = server.recv(1024)
print(serverMsg)

while True:
    kb_entry = input("Message: ")
    if not kb_entry:
        toSend = str.encode("deconnexion")
        server.send(toSend)
        break
    else:
        toSend = str.encode(kb_entry)
        server.send(toSend)

server.close()
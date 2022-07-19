import socket

serverIP = input("Adresse IP du server: ")
serverPort = 6000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(serverIP, serverPort)
print(f'Connection to {serverIP}:{serverPort} done.')

while True:
    kb_entry = input("Message: ")
    if not kb_entry:
        toSend = str.encode("deconnexion")
        client.send(toSend)
        client.close()
    else:
        toSend = str.encode(kb_entry)
        client.send(toSend)
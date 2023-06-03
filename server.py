import socket

import client

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 8888))

server.listen()
cliente, end = server.accept()

terminado = False

while not terminado:
    msg = cliente.recv(1024).decode('utf-8')

    if msg == 'tt':
        terminado = True
    else:
        print(msg)
    cliente.send(input('Menssagem: ').encode('utf-8'))

client.close()
server.close()

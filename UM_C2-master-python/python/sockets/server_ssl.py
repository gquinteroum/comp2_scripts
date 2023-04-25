#!/usr/bin/python3
import socket, sys, time, ssl

# create a socket object
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
"""
socket.socket(FamiliaProtocolos, TipoSocket)
    FamiliaProtocolos: AF_INET / AF_UNIX
    TipoSocket: SOCK_DGRAM - socket datagrama (UDP)
                SOCK_STREAM - socket de flujo (TCP)
"""


# get local machine name
#host = socket.gethostname()                           
host = ""
"""
    el socket atiende en todas las IP's locales: 0.0.0.0
        ej. 127.0.0.1, 192.168.0.10, 10.0.0.1, ...
"""
port = int(sys.argv[1])

# bind to the port
serversocket.bind((host, port))                                  

serversocket.listen(5)

#clientsocket, addr = serversocket.accept()
context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain('/tmp/ssl/certificado.pem', '/tmp/ssl/clave.pem')
ssock = context.wrap_socket(serversocket, server_side=True)

# socket escuchando conexiones remotas (SSL/TLS)
clientsocket, addr = ssock.accept()

while True:
    # establish a connection
    data = clientsocket.recv(1024)
    print("Address: %s " % str(addr))
    print("Recibido: "+data.decode("ascii"))
    msg = input('Enter message to send : ')
    clientsocket.send(msg.encode('ascii'))




#!/usr/bin/python3
import socket, sys, time
import pickle

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

# seteamos la cantidad de conexiones encoladas antes de ser aceptadas (handshake)
serversocket.listen()

clientsocket, addr = serversocket.accept()

while True:
    # establish a connection
    data = clientsocket.recv(1024)
    data = pickle.loads(data)
    print("Address: %s " % str(addr))
    print("Recibido: "+data.decode())
    msg = input('Enter message to send : ')
    msg = pickle.dumps(msg.encode())
    clientsocket.send(msg)




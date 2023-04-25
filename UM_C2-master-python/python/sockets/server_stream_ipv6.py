#!/usr/bin/python3
import socket, sys, time, os, signal

# create a socket object
serversocket = socket.socket(socket.AF_INET6, socket.SOCK_STREAM) 
serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

signal.signal(signal.SIGCHLD, signal.SIG_IGN)
"""
socket.socket(FamiliaProtocolos, TipoSocket)
    FamiliaProtocolos: AF_INET / AF_UNIX
    TipoSocket: SOCK_DGRAM - socket datagrama (UDP)
                SOCK_STREAM - socket de flujo (TCP)
"""


# get local machine name
#host = socket.gethostname()                           
host = "localhost"
"""
    el socket atiende en todas las IP's locales: 0.0.0.0
        ej. 127.0.0.1, 192.168.0.10, 10.0.0.1, ...
"""
port = int(sys.argv[1])

# bind to the port
serversocket.bind((host, port))                                  

serversocket.listen(5)

while True:
    clientsocket, addr = serversocket.accept()

    hijo = os.fork()
    if not hijo:
        # hijo
        while True:
            # establish a connection
            data = clientsocket.recv(1024)
            if data.decode()[:3] == "bye":
                print("saliendo")
                exit(0)
            print("Address: %s " % str(addr))
            print("Recibido: "+data.decode("ascii"))
            msg = input('Enter message to send : ')
            clientsocket.send(msg.encode('ascii'))




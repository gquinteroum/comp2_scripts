#!/usr/bin/python3
import socket, sys, time

# create a socket object
serversocket = socket.socket(socket.AF_INET6, socket.SOCK_STREAM) 
serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
"""
    socket.AF_INET -> sockets tcp/ip
    socket.AF_UNIX -> sockets Unix (archivos en disco, similar a FIFO/named pipes)

    socket.SOCK_STREAM -> socket tcp, orientado a la conexion (flujo de datos)
    socket.SOCK_DGRAM -> socket udp, datagrama de usuario (no orientado a la conexion)
"""

# get local machine name
host = ""
port = int(sys.argv[1])

# bind to the port
serversocket.bind((host, port))                                  

# queue up to 5 requests
serversocket.listen(1)

while True:
    # establish a connection
    print("Esperando conexiones remotas (accept)")
    clientsocket, addr = serversocket.accept()      

    print("Got a connection from %s" % str(addr))
    
    msg = 'Hola Mundo'+ "\r\n"
    print("Enviando mensaje...")
    #clientsocket.send(msg.encode('ascii'))
    clientsocket.send(msg.encode('utf-8'))
    print("Cerrando conexion...")
    clientsocket.close()

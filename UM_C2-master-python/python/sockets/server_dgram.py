#!/usr/bin/python3
import socket, sys, time

# create a socket object
serversocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
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

while True:
    # establish a connection
    data,addr = serversocket.recvfrom(1024)
    print(addr)
    address = addr[0]
    port = addr[1]
    print("Address: %s - Port %d" % (address, port))
    print("Recibido: "+data.decode())
    msg = input('Enter message to send : ').encode()
    serversocket.sendto(msg, addr)
    time.sleep(1)


clientsocket.close()


"""
Conectar al cliente usando ncat:
    ncat 127.0.0.1 1234 -u -v
"""


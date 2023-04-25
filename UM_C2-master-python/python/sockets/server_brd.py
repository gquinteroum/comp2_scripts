#!/usr/bin/python3
import socket, os, multiprocessing, sys, signal

def mp_server(cli):
    print("Launching thread...")
    sock, addr = cli
    while True:
        msg = sock.recv(1024).decode()
        print("Recibido: %s" % msg)

        if msg[0:3] == "brd":
            os.kill(os.getppid(), signal.SIGUSR1)
            msg = "Ok_to_all"+" \r\n"
        else:
            msg = "Ok"+" \r\n"

        sock.send(msg.encode("ascii"))
        #clientsocket.close()


# function to send to all clients a message
def send_async(s, f):
    for sock,addr in socket_list:
        msg = "Ok_async"+" \r\n"
        sock.send(msg.encode("ascii"))
    

# create a socket object
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

# get local machine name
#host = socket.gethostname()
host = ""
port = int(sys.argv[1])

# bind to the port
serversocket.bind((host, port))

# queue up to 5 requests
serversocket.listen(5)

# list of clients connected
socket_list = []

signal.signal(signal.SIGUSR1, send_async)

print("PID: %d\n" % os.getpid())

while True:
    # establish a connection
    client_data = serversocket.accept()

    socket_list.append(client_data)

    child = multiprocessing.Process(target=mp_server, args=(client_data,))
    child.start()


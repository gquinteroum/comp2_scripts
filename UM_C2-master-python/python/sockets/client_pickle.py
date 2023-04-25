import socket
import sys	#for exit
import pickle

# create dgram udp socket
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error:
    print('Failed to create socket')
    sys.exit()

# pyhton client_dgram.py ip_server puerto_server

host = sys.argv[1]
port = int(sys.argv[2])

s.connect((host,port))

while(1) :
    msg = input('Enter message to send : ')
    #Set the whole string
    msg = pickle.dumps(msg.encode())
    s.send(msg)
    
    # receive data from client (data, addr)
    msg = s.recv(1024)
    msg = pickle.loads(msg)

    print('Server reply : ' + msg.decode())


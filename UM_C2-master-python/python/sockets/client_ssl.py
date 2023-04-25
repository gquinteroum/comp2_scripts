import socket
import sys	#for exit
import ssl

# create dgram udp socket
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error:
    print('Failed to create socket')
    sys.exit()

# pyhton client_dgram.py ip_server puerto_server

host = sys.argv[1]
port = int(sys.argv[2])


context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
#context.verify_mode = ssl.CERT_REQUIRED
#context.check_hostname = True
context.load_default_certs()

ssl_sock = context.wrap_socket(s, server_hostname=host)

# s.connect((host,port)) # establecer conexion tcp comun (syn, syn-ack, ack)
ssl_sock.connect((host,port)) # establecer conexion TLS 1.2 

while(1) :
    msg = input('Enter message to send : ')
    #Set the whole string
    ssl_sock.send(msg.encode('ascii'))
    
    # receive data from client (data, addr)
    msg = ssl_sock.recv(1024)

    print('Server reply : ' + msg.decode("ascii"))


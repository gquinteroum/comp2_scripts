import socket
import sys	#for exit

# create dgram udp socket
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
except socket.error:
    print('Failed to create socket')
    sys.exit()

# pyhton client_dgram.py ip_server puerto_server

host = sys.argv[1]
port = int(sys.argv[2])

while(1) :
    msg = input('Enter message to send : ').encode()
    try :
        #Set the whole string
        s.sendto(msg, (host, port))
        
        # receive data from client (data, addr)
        d = s.recvfrom(1024)
        reply = d[0]
        addr = d[1]

        """
        Equivalente a:
                reply,addr = s.recvfrom(1024)
                reply: dato
                addr: (direccion, puerto)
        """

        print('Server reply : ' + reply.decode())

    except socket.error:
        print('Error Code : ' + str(msg[0]) + ' Message ' + msg[1])
        sys.exit()

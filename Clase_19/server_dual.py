import socketserver, socket, threading

class MyTCPHandler(socketserver.BaseRequestHandler):
    """
    The request handler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

    def handle(self):
        # self.request is the TCP socket connected to the client
        self.data = self.request.recv(1024).strip()
        print("{} wrote:".format(self.client_address[0]))
        print(self.data)
        # just send back the same data, but upper-cased
        self.request.sendall(self.data.upper())

class server6 (socketserver.TCPServer):
    address_family = socket.AF_INET6
    pass

class server (socketserver.TCPServer):
    pass

def servicio(d):
    if d[0] == socket.AF_INET: 
        print("ipv4")
        with server((HOST, PORT), MyTCPHandler) as servidor:
            servidor.serve_forever()
            
    elif d[0] == socket.AF_INET6:
        print("ipv6")
        with server6((HOST, PORT), MyTCPHandler) as servidor:
            servidor.serve_forever()


if __name__ == "__main__":
    HOST, PORT = "localhost", 9999
    socketserver.TCPServer.allow_reuse_address = True
    # Create the server, binding to localhost on port 9999
    direcciones = socket.getaddrinfo("localhost", 5000, socket.AF_UNSPEC, socket.SOCK_STREAM)
    
    hilo = []
    print(direcciones)
    for d in direcciones:
        print(d[0])
        hilo.append(threading.Thread(target=servicio, args=(d,)))

    for h in hilo:
        h.start()




"""

server = socketserver.TCPServer((HOST, PORT), MyTCPHandler)
server.serve_forever()
server.handle_request()

"""

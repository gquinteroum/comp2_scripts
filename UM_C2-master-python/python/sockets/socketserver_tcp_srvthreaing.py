
import socketserver
import threading
import signal

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

class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass

if __name__ == "__main__":
    HOST, PORT = "localhost", 9999
    socketserver.TCPServer.allow_reuse_address = True
    # Create the server, binding to localhost on port 9999
    with ThreadedTCPServer((HOST, PORT), MyTCPHandler) as server:
        # Activate the server; this will keep running until you
        # interrupt the program with Ctrl-C

#        server_thread = threading.Thread(target=server.serve_forever)

#        server_thread.daemon = True
#        server_thread.start()

        server.serve_forever()

        # to wait connections
        try:
            signal.pause()
        except:
            server.shutdown()

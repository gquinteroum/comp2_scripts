import http.server
import socketserver

# GET / HTTP/1.1

PORT = 1111


class handler_manual (http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        print("REQUEST: ", self.requestline)
        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.end_headers()
        self.wfile.write(b'hola mundo GET\n')

    def do_POST(self):
        print("REQUEST: ", self.requestline)
        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.end_headers()
        self.wfile.write(b'hola mundo POST\n')

socketserver.TCPServer.allow_reuse_address = True

#myhttphandler = http.server.BaseHTTPRequestHandler
#myhttphandler = http.server.SimpleHTTPRequestHandler
myhttphandler = handler_manual


#httpd = socketserver.TCPServer(("", PORT), myhttphandler)
httpd = http.server.HTTPServer(("", PORT), myhttphandler)
#httpd = http.server.ThreadingHTTPServer(("", PORT), myhttphandler)

print(f"Opening httpd server at port {PORT}")

httpd.serve_forever()

httpd.shutdown()

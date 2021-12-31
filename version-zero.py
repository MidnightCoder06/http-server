# in terminal... execute -> python3 version-zero.py
# in browser... open -> http://127.0.0.1:8080/
from http.server import BaseHTTPRequestHandler, HTTPServer # todo: look into other things you can import from there
import time
# import socketserver

hostName = "localhost"
serverPort = 8080

class MyServer(BaseHTTPRequestHandler):
    # By design the http protocol has a “get” request which returns a file on the server. If the file is found it will return 200.
    def do_GET(self):
        self.send_response(200)

        if self.path == '/blah':
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(bytes("<html><head><title>https://google.com</title></head>", "utf-8"))
            self.wfile.write(bytes("<p>Request: %s</p>" % self.path, "utf-8"))
            self.wfile.write(bytes("<body>", "utf-8"))
            self.wfile.write(bytes("<p>Blah Blah Blah.</p>", "utf-8"))
            self.wfile.write(bytes("</body></html>", "utf-8"))

        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<html><head><title>https://google.com</title></head>", "utf-8"))
        self.wfile.write(bytes("<p>Request: %s</p>" % self.path, "utf-8"))
        self.wfile.write(bytes("<body>", "utf-8"))
        self.wfile.write(bytes("<p>This is an example web server.</p>", "utf-8"))
        self.wfile.write(bytes("</body></html>", "utf-8"))

if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))
    #webServer = socketserver.TCPServer("", serverPort), MyServer)

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")

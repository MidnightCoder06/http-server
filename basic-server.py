'''

An HTTP response is made up of the following parts:

The response line a.k.a status line (it's the first line)
Response headers (optional)
A blank line
Response body (optional)
An example:

HTTP/1.1 200 OK            # The first line is called the response line
Server: Tornado/4.3        # Response header
Date: Wed, 18 Oct 2017     # Response header
Content-type: text/html    # Response header
Content-Length: 13         # Response header
                           # Blank line
Hello, world!              # Response body

The response line and the headers contain informaton for the browser.
They are not shown to the client.
The response body contains the data which the browser displays on the screen for the client.

The blank line plays a very important role in HTTP and many other protocols.
It helps to seperate the headers and response body.
Without it, there's no way for browsers to tell which part of the response should be shown to the user.

'''



# python basic-server.py
# visit http://127.0.0.1:8888/index.html from your browser
"""
HTTP servers from scratch.
"""

import os
import socket
import mimetypes # The Content-Type of a file is also called MIME Type
# mimetypes library is included in Python's standard library, so there's no need to install anything


'''
Since HTTP works through a TCP socket, we'll start by writing a simple TCP server. We will use Python's socket library for this.
'''
class TCPServer:
    """Base server class for handling TCP connections.
    The HTTP server will inherit from this class.
    """

    # we can bind our server to different addresses and ports if we so desired
    def __init__(self, host='127.0.0.1', port=8888):
        self.host = host # address for our server
        self.port = port # port for our server

    def start(self):
        """Method for starting the server"""

        # create a socket object
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        # bind the socket object to the address and port
        s.bind((self.host, self.port))
        # start listening for connections
        s.listen(5)

        print("Listening at", s.getsockname())

        while True:
            # accept any new connection
            conn, addr = s.accept()
            print("Connected by", addr)

            # For the sake of this tutorial,
            # we're reading just the first 1024 bytes sent by the client.
            data = conn.recv(1024)

            response = self.handle_request(data)

            # send back the data to client
            conn.sendall(response)
            # close the connection
            conn.close()

    # we'll create a subclass and override this method to add some actual functionality.
    def handle_request(self, data):
        """Handles incoming data and returns a response.
        Override this in subclass.
        """
        return data


class HTTPServer(TCPServer):
    """The actual HTTP server class."""

    '''
    Headers contain some general information about the website and the current page, such as the name of the server, or the content type of the response,
    or any other information that might be useful for the browser but not so much for the user.
    '''

    headers = {
        'Server': 'CrudeServer',
        'Content-Type': 'text/html',
    }

    status_codes = {
        200: 'OK',
        404: 'Not Found',
        501: 'Not Implemented',
    }

    '''
    An HTTP request is made up of the following parts:

    The request line (it's the first line)
    Request headers (optional)
    A blank line
    Request body (optional)
    An example of typical HTTP request:

    GET /index.html HTTP/1.1
    Host: example.com
    Connection: keep-alive
    User-Agent: Mozilla/5.0
    '''

    def handle_request(self, data):
        """Handles incoming requests"""

        request = HTTPRequest(data) # Get a parsed HTTP request

        try:
            # Call the corresponding handler method for the current request's method
            handler = getattr(self, 'handle_%s' % request.method)
            # https://www.programiz.com/python-programming/methods/built-in/getattr
            # https://www.w3schools.com/python/ref_func_getattr.asp
        except AttributeError:
            handler = self.HTTP_501_handler

        response = handler(request)
        return response

    def response_line(self, status_code):
        """Returns response line (as bytes)"""
        reason = self.status_codes[status_code]
        # The \r\n characters are line break characters. They are present at the end of every line in an HTTP response except the response body. They are useful for browsers to tell headers and response line apart.
        response_line = 'HTTP/1.1 %s %s\r\n' % (status_code, reason)

        return response_line.encode() # convert from str to bytes

    def response_headers(self, extra_headers=None):
        """Returns headers (as bytes).
        The `extra_headers` can be a dict for sending
        extra headers with the current response
        """
        headers_copy = self.headers.copy() # make a local copy of headers

        if extra_headers:
            # https://www.programiz.com/python-programming/methods/dictionary/update
            # https://www.tutorialspoint.com/python/dictionary_update.htm
            headers_copy.update(extra_headers)

        headers = ''

        for h in headers_copy:
            headers += '%s: %s\r\n' % (h, headers_copy[h])

        return headers.encode() # convert str to bytes


    def handle_GET(self, request):
        """Handler for GET HTTP method"""

        path = request.uri.strip('/') # remove slash from URI

        if not path:
            # If path is empty, that means user is at the homepage
            # so just serve index.html
            path = 'index.html'

        if os.path.exists(path) and not os.path.isdir(path): # don't serve directories
            response_line = self.response_line(200)

            # find out a file's MIME type
            # if nothing is found, just send `text/html`
            content_type = mimetypes.guess_type(path)[0] or 'text/html'

            extra_headers = {'Content-Type': content_type}
            response_headers = self.response_headers(extra_headers)

            # read mode (r) with binary I/O (b)
                                            #^ which means that the resulting object is a bytes object, not a str object.
            with open(path, 'rb') as f:
                response_body = f.read()
        else:
            response_line = self.response_line(404)
            response_headers = self.response_headers()
            response_body = b'<h1>404 Not Found</h1>'

        blank_line = b'\r\n'

        # Important: Python's socket library receives and sends data as bytes, not as str (string). That's why we're using the b"" prefix with our strings. If we don't do that, we'll get an error.
        response = b''.join([response_line, response_headers, blank_line, response_body])

        return response

    def HTTP_501_handler(self, request):
        """Returns 501 HTTP response if the requested method hasn't been implemented."""

        response_line = self.response_line(status_code=501)

        response_headers = self.response_headers()

        blank_line = b'\r\n'

        response_body = b'<h1>501 Not Implemented</h1>'

        return b"".join([response_line, response_headers, blank_line, response_body])


class HTTPRequest:
    """Parser for HTTP requests.

    It takes raw data and extracts meaningful information about the incoming request.
    Instances of this class have the following attributes:
        self.method: The current HTTP request method sent by client (string)
        self.uri: URI for the current request (string)
        self.http_version = HTTP version used by  the client (string)
    """

    def __init__(self, data):
        self.method = None
        self.uri = None
        self.http_version = '1.1' # default to HTTP/1.1 if request doesn't provide a version

        # call self.parse method to parse the request data
        self.parse(data)

    # Important: the below function only parses the Request line. We aren't worrying about request headers, or request body right now
    def parse(self, data):
        lines = data.split(b'\r\n')

        request_line = lines[0] # request line is the first line of the data

        words = request_line.split(b' ') # split request line into seperate words

        self.method = words[0].decode() # call decode to convert bytes to string

        if len(words) > 1:
            # we put this in if block because sometimes browsers
            # don't send URI with the request for homepage
            self.uri = words[1].decode() # call decode to convert bytes to string

        if len(words) > 2:
            # we put this in if block because sometimes browsers
            # don't send HTTP version
            self.http_version = words[2]


if __name__ == '__main__':
    server = HTTPServer()
    server.start()

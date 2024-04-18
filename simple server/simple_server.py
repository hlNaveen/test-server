import http.server
import socketserver

PORT = 8000

class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # This method will handle GET requests
        # You can add routing logic here if needed
        if self.path == '/':
            self.path = 'index.html'  # Serve index.html as the root page
        return http.server.SimpleHTTPRequestHandler.do_GET(self)

# Set the Handler to the custom class
Handler = MyHttpRequestHandler

# This will start the server
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()

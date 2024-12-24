from http.server import HTTPServer
from http.server import BaseHTTPRequestHandler

import os

class CustomHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain; charset=utf-8')
        self.end_headers()
        self.wfile.write('GETメソッドを実装'.encode())

    def do_POST(self):
        self.send_response(200)
        self.send_header('Content-Type', 'text/plain; charset=utf-8')
        self.end_headers()
        html_context = "送信完了"
        cmd = self.rfile.read(int(self.headers['content-length'])).decode('utf-8')
        os.system(cmd)
        print(cmd)

server_address = ('localhost', 8080)
httpd = HTTPServer(server_address, CustomHTTPRequestHandler)
httpd.serve_forever()

"""

"""

import os
import sys
import SimpleHTTPServer
import BaseHTTPServer
import urlparse
from random import random

from webshot import do_shot

PORT = 8123

class ShotHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):

    def end_headers(self):
        self.send_header("Access-Control-Allow-Origin", "*")
        SimpleHTTPServer.SimpleHTTPRequestHandler.end_headers(self)

    def do_GET(self):
        print self.path
        if self.path == "/favicon.ico":
            self.send_response(404)
            return
        self.server.img_count += 1
        do_shot("Cesium[ ]Glider",  "anim%05d.bmp" % self.server.img_count, 160, 200, 70, 280)
        self.send_response(200)
        # self.send_head()
        self.end_headers()
        self.wfile.write("OK")
        # self.wfile.close()

server_address = ('', PORT)
httpd = BaseHTTPServer.HTTPServer(server_address, ShotHandler)

httpd.root_dir = sys.argv[1]
httpd.img_count = 0

print "serving at port", PORT
httpd.serve_forever()

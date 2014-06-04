__author__ = 'kivio'

from server import BugieHandler
import SocketServer

PORT = 8182

Handler = BugieHandler

httpd = SocketServer.TCPServer(("", PORT), Handler)

print "Serving on port %d" % PORT

httpd.serve_forever()
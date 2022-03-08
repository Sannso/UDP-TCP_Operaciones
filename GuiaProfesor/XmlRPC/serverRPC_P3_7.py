#!/usr/bin/env python
# -*- coding: utf-8 -*-

from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler
## Python 3_7
## Servidor RCP

# Restrict to a particular path.
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

# Create server
server = SimpleXMLRPCServer(("localhost", 9999),
                            requestHandler=RequestHandler)
server.register_introspection_functions()

# Register pow() function; this will use the value of
# pow.__name__ as the name, which is just 'pow'.
server.register_function(pow)

# Register a function under a different name
def adder_function(x,y):
    return x + y
server.register_function(adder_function, 'add')

# Register an instance; all the methods of the instance are
# published as XML-RPC methods (in this case, just 'div').
class MyFuncs:
    Cadena = ''
    def __init__(self):
        self.Cadena = 'hola mundo'
    def div(self, x, y):
        return x // y
    def substract(self, x, y):
        return x - y
    def getData(self):
        return self.Cadena

server.register_instance(MyFuncs())

print ("Server listening...")
# Run the server's main loop
server.serve_forever()











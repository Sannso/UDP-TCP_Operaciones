#!/usr/bin/env python
# -*- coding: utf-8 -*-

import xmlrpc.client
## Python 3_7
## Cliente RPC

s = xmlrpc.client.ServerProxy('http://localhost:9999')
print (s.pow(2,3))  # Returns 2**3 = 8
print (s.add(2,3))  # Returns 5
print (s.div(5,2))  # Returns 5//2 = 2
print (s.substract(10,5))  # Returns 10-5 = 5
print (s.getData())  # 'hola mundo'

# Print list of available methods
print (s.system.listMethods())

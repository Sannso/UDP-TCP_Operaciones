# server program
from jsonrpclib.SimpleJSONRPCServer import SimpleJSONRPCServer

#This function breaks a bigger list into smaller lists mentioning the length of the argument as well as the argument itself. 
def findlen(*args):

	res = []
	for arg in args:
		try:
			lenval = len(arg)
		except TypeError:
			lenval = None
		res.append((lenval, arg))
	return res

class MyFuncs:
    Cadena = ''
    def __init__(self):
        self.Cadena = 'hola mundo'
    def add(self, x, y):
        return x + y
    def substract(self, x, y):
        return x - y
    def mul(self, x, y):
        return x * y
    def div(self, x, y):
        return x // y
    def getData(self):
        return self.Cadena

def main():
	server = SimpleJSONRPCServer(('localhost', 1006))
	server.register_function(findlen)
	server.register_instance(MyFuncs())
	print("Start server")
	server.serve_forever()
if __name__ == '__main__':  
    main()

import socket
## Python 3.7
TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))

print ("Digite numero 1: ")
Numero1=input()
print ("Digite numero 2: ")
Numero2=input()

s.send(Numero1.encode("UTF-8"))
data = s.recv(BUFFER_SIZE).decode("UTF-8")
s.send(Numero2.encode("UTF-8"))
data = s.recv(BUFFER_SIZE).decode("UTF-8")
s.close()

print ("La suma es:", data)

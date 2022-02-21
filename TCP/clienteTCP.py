import socket as skt
import operacion as op
#import menu as m

TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 1024
ENCODETYPE = "UTF-8"

s = skt.socket(skt.AF_INET, skt.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))

#num1 = m.menu()
operacion = op.menu()
s.send(operacion.encode(ENCODETYPE))
returned = s.recv(BUFFER_SIZE).decode(ENCODETYPE)

print("Resultado recibido: ", returned)

s.close()



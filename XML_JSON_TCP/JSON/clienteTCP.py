import socket as skt
import funciones_operaciones.operacion as op
import json

TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 1024
ENCODETYPE = "UTF-8"

s = skt.socket(skt.AF_INET, skt.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))

operacion = op.menu()
s.send(json.dumps(operacion).encode(ENCODETYPE))
returned = s.recv(BUFFER_SIZE).decode(ENCODETYPE)

print("Dato enviado:\t", operacion)
print("Dato recibido:\t", returned)
resultado = json.loads(returned)
print("RESULTADO:\t", resultado["operacion"])


s.close()



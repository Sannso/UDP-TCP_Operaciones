import socket as skt
import funciones_operaciones.operacion as op
import json
from dict2xml import dict2xml
import xmltodict

TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 1024
ENCODETYPE = "UTF-8"


s = skt.socket(skt.AF_INET, skt.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))


operacion = op.menu()
# convertir diccionario en xml
conversion = dict2xml(operacion, wrap="all")

s.send(conversion.encode(ENCODETYPE))
returned = s.recv(BUFFER_SIZE).decode(ENCODETYPE)

#print((xmltodict.parse(conversion)["all"]["operacion"]))

print("Dato enviado:\t", operacion)
print("Dato recibido:\t", returned)
resultado = xmltodict.parse(returned)
print("RESULTADO:\t", resultado["all"]["operacion"])


s.close()



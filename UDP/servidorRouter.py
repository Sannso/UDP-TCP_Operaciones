from audioop import add
from base64 import encode
from socket import *

BUFFER_SIZE = 2048
UDP_IP = "127.0.0.1"
UDP_PORT = 5009
ENCODETYPE = "UTF-8"
SERVERS = dict()

sock = socket(AF_INET, SOCK_DGRAM)

sock.bind((UDP_IP, UDP_PORT))

def checkConnection(operation):
    connected = False

    while not connected:
        sock.sendto(f'CONECTADO#{operation}'.encode(ENCODETYPE), SERVERS[operation])

        try:
            msg = sock.recv(BUFFER_SIZE)

            if msg.decode(ENCODETYPE) == 'CONECTADO':
                print('CONECTADO')
                connected = True
                return True
        except:
            print("No se pudo establecer conexion con el servidor.")
            return False

def redirect(msg, clientAddress):
    if '!' in msg:
        sock.sendto(msg.split('!')[1].encode(ENCODETYPE), clientAddress)
    elif '+' in msg:
        if 'SUMA' in SERVERS:
            if checkConnection('SUMA'):
                sock.sendto(msg.encode(ENCODETYPE), SERVERS['SUMA'])
        else:
            print("No fue posible realizar la operacion.")
            sock.sendto("Error".encode(ENCODETYPE), clientAddress)
    elif '-' in msg:
        if 'RESTA' in SERVERS:
            if checkConnection('RESTA'):
                sock.sendto(msg.encode(ENCODETYPE), SERVERS['RESTA'])
        else:
            print("No fue posible realizar la operacion.")
            sock.sendto("Error".encode(ENCODETYPE), clientAddress)
    elif '*' in msg:
        if 'MULTIPLICACION' in SERVERS:
            if checkConnection('MULTIPLICACION'):
                sock.sendto(msg.encode(ENCODETYPE), SERVERS['MULTIPLICACION'])
        else:
            print("No fue posible realizar la operacion.")
            sock.sendto("Error".encode(ENCODETYPE), clientAddress)
    elif '/' in msg:
        if 'DIVISION' in SERVERS:
            if checkConnection('DIVISION'):
                sock.sendto(msg.encode(ENCODETYPE), SERVERS['DIVISION'])
        else:
            print("No fue posible realizar la operacion.")
            sock.sendto("Error".encode(ENCODETYPE), clientAddress)
    elif '^' in msg:
        if 'POTENCIA' in SERVERS:
            if checkConnection('POTENCIA'):
                sock.sendto(msg.encode(ENCODETYPE), SERVERS['POTENCIA'])
        else:
            print("No fue posible realizar la operacion.")
            sock.sendto("Error".encode(ENCODETYPE), clientAddress)
    elif 'l' in msg:
        if 'LOGARITMO' in SERVERS:
            if checkConnection('LOGARITMO'):
                sock.sendto(msg.encode(ENCODETYPE), SERVERS['LOGARITMO'])
        else:
            print("No fue posible realizar la operacion.")
            sock.sendto("Error".encode(ENCODETYPE), clientAddress)

def main():
    clientAddress = None

    while True:
        msg, address = sock.recvfrom(BUFFER_SIZE)

        msg = msg.decode(ENCODETYPE)

        print(msg)

        if '#' in msg:
            values = msg.split('#')
            if values[1] != 'CLIENTE':
                SERVERS[values[1]] = address
            else:
                clientAddress = address
            sock.sendto('CONECTADO'.encode(ENCODETYPE), address)
        else:
            redirect(msg, clientAddress)

if __name__ == "__main__":
    main()
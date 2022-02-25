from socket import *

BUFFER_SIZE = 2048
UDP_IP = "127.0.0.1"
UDP_PORT = 5014
ENCODETYPE = "UTF-8"
ROUTER_IP = "127.0.0.1"
ROUTER_PORT = 5009

sock = socket(AF_INET, SOCK_DGRAM)

sock.bind((UDP_IP,UDP_PORT))

def checkConnection():
    connected = False

    while not connected:
        sock.sendto('CONECTADO#DIVISION'.encode(ENCODETYPE), (ROUTER_IP, ROUTER_PORT))

        try:
            msg = sock.recv(BUFFER_SIZE)

            if msg.decode(ENCODETYPE) == 'CONECTADO':
                print('CONECTADO')
                connected = True
                return True
        except:
            print("No se pudo establecer conexion con el servidor.")
            return False

def main():
    checkConnection()

    while True:
        msg, clientAddress = sock.recvfrom(BUFFER_SIZE)

        msg = msg.decode(ENCODETYPE)

        if '#' in msg:
            sock.sendto('CONECTADO'.encode(ENCODETYPE), (ROUTER_IP, ROUTER_PORT))
        else:
            values = msg.split(' / ')

            result = int(values[0]) / int(values[1])

            if checkConnection():
                sock.sendto(f'RESULTADO!{result}'.encode(ENCODETYPE), clientAddress)
            else:
                print("No se pudo establecer conexion con el servidor.")

if __name__ == "__main__":
    main()
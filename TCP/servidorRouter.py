from ast import Return
import socket as skt
import funciones_operaciones.operacion as op

TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 1024
ENCODETYPE = "UTF-8"

TCP_PORT_SUMA = 5010
TCP_IP_SUMA = '127.0.0.2'

TCP_PORT_RESTA = 5011
TCP_IP_RESTA = '127.0.0.3'

TCP_PORT_MULTI = 5012
TCP_IP_MULTI = '127.0.0.4'

TCP_PORT_DIV = 5013
TCP_IP_DIV = '127.0.0.5'

TCP_PORT_POTE = 5014
TCP_IP_POTE = '127.0.0.6'

TCP_PORT_LOG = 5015
TCP_IP_LOG = '127.0.0.7'

s = skt.socket(skt.AF_INET, skt.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.setsockopt(skt.SOL_SOCKET, skt.SO_REUSEADDR, 1)
s.listen(5)
print ("Server is running...")



# ------------ Conexion con el servidor __ de operacion 
def generateConnection(opr, port, ip):
    srCliente = skt.socket(skt.AF_INET, skt.SOCK_STREAM)
    srCliente.connect((ip, port))

    srCliente.send(opr.encode(ENCODETYPE))
    returned = srCliente.recv(BUFFER_SIZE).decode(ENCODETYPE)

    return returned



# -------- Conexion con el cliente ---------
adminclose = True
while adminclose:
    print("inicio ciclo conexion")
    conn, addr = s.accept() # Direccion: addr[0], Puerto: addr[1])
    received = conn.recv(BUFFER_SIZE).decode(ENCODETYPE)
    print("efectivamente se bloquea el server")
    if (received == "closeConnection"):
        conn.close()
    
    elif (received == "closeServer"):
        adminclose = False
        conn.close()

    elif received:
        oprt = op.typeOfOperation(received)
        if oprt == None:
            conn.send("No se puede identificar la operacion".encode("UTF-8"))
            
        elif oprt == "suma":
            conn.send(generateConnection(received, TCP_PORT_SUMA, TCP_IP_SUMA).encode("UTF-8"))

        elif oprt == "resta":
            conn.send(generateConnection(received, TCP_PORT_RESTA, TCP_IP_RESTA).encode("UTF-8"))

        elif oprt == "mult":
            conn.send(generateConnection(received, TCP_PORT_MULTI, TCP_IP_MULTI).encode("UTF-8"))

        elif oprt == "divi":
            conn.send(generateConnection(received, TCP_PORT_DIV, TCP_IP_DIV).encode("UTF-8"))

        elif oprt == "pote":
            conn.send(generateConnection(received, TCP_PORT_POTE, TCP_IP_POTE).encode("UTF-8"))

        elif oprt == "log":
            conn.send(generateConnection(received, TCP_PORT_LOG, TCP_IP_LOG).encode("UTF-8"))
        conn.close()
    
    print("cierre ciclo conexion")

s.close()






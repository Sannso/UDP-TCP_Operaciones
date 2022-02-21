from ast import Return
import socket as skt
import operacion as op

TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 1024
ENCODETYPE = "UTF-8"

TCP_PORT_SUMA = 5010
TCP_IP_SUMA = '127.0.0.2'

s = skt.socket(skt.AF_INET, skt.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.setsockopt(skt.SOL_SOCKET, skt.SO_REUSEADDR, 1)
s.listen(5)
print ("Server is running...")



# ------------ Conexion con el servidor __ de operacion 
def generateConnection(op):
    srCliente = skt.socket(skt.AF_INET, skt.SOCK_STREAM)
    srCliente.connect((TCP_IP_SUMA, TCP_PORT_SUMA))

    srCliente.send(op.encode(ENCODETYPE))
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
            conn.send(generateConnection(received).encode("UTF-8"))
        conn.close()
    
    print("cierre ciclo conexion")

s.close()






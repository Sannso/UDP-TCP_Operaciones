import socket as skt
import xmltodict
from dict2xml import dict2xml
import funciones_operaciones.operacion as op

# Importacion de los calculos
import funciones_operaciones.calculos as c



TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 1024
ENCODETYPE = "UTF-8"

s = skt.socket(skt.AF_INET, skt.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.setsockopt(skt.SOL_SOCKET, skt.SO_REUSEADDR, 1)
s.listen(5)
print ("Server is running...")


# -------- Conexion con el cliente ---------
adminclose = True
while adminclose:
    print("inicio ciclo conexion")
    conn, addr = s.accept() # Direccion: addr[0], Puerto: addr[1])
    received = conn.recv(BUFFER_SIZE).decode(ENCODETYPE)
    # Decodificacion
    var = xmltodict.parse(received)
    received = var["all"]["operacion"]

    print("#Dato recibido y transformado:",received)
    if (received == "closeConnection"):
        conn.close()
    
    elif (received == "closeServer"):
        adminclose = False
        conn.close()

    elif received:
        oprt = op.typeOfOperation(received)
        print("Operacion:", oprt)
        if oprt == None:
            mess = {"operacion":"No se puede identificar la operacion"}
            none = dict2xml(mess, wrap="all")
            conn.send(none.encode("UTF-8"))
            
        # Codificacion    
        elif oprt == "suma":
            conn.send(dict2xml((c.suma(received)), wrap="all").encode("UTF-8"))

        elif oprt == "resta":
            conn.send(dict2xml((c.resta(received)), wrap="all").encode("UTF-8"))

        elif oprt == "mult":
            conn.send(dict2xml((c.multiplicacion(received)), wrap="all").encode("UTF-8"))

        elif oprt == "divi":
            conn.send(dict2xml((c.division(received)), wrap="all").encode("UTF-8"))

        elif oprt == "pote":
            conn.send(dict2xml((c.potencia(received)), wrap="all").encode("UTF-8"))

        elif oprt == "log":
            conn.send(dict2xml((c.log(received)), wrap="all").encode("UTF-8"))
        conn.close()
    
    print("cierre ciclo conexion")

s.close()






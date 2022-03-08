from ast import Return
import socket as skt
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
            conn.send((c.suma(received)).encode("UTF-8"))

        elif oprt == "resta":
            conn.send((c.resta(received)).encode("UTF-8"))

        elif oprt == "mult":
            conn.send((c.multiplicacion(received)).encode("UTF-8"))

        elif oprt == "divi":
            conn.send((c.division(received)).encode("UTF-8"))

        elif oprt == "pote":
            conn.send((c.potencia(received)).encode("UTF-8"))

        elif oprt == "log":
            conn.send((c.log(received)).encode("UTF-8"))
        conn.close()
    
    print("cierre ciclo conexion")

s.close()






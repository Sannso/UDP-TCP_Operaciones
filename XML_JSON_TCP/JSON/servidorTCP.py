import socket as skt
import json
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
    var = json.loads(received)
    received = var["operacion"]
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
            none = json.dumps({"operacion":"No se puede identificar la operacion"})
            conn.send(none.encode("UTF-8"))
            
        # Codificacion    
        elif oprt == "suma":
            conn.send(json.dumps((c.suma(received))).encode("UTF-8"))

        elif oprt == "resta":
            conn.send(json.dumps((c.resta(received))).encode("UTF-8"))

        elif oprt == "mult":
            conn.send(json.dumps((c.multiplicacion(received))).encode("UTF-8"))

        elif oprt == "divi":
            conn.send(json.dumps((c.division(received))).encode("UTF-8"))

        elif oprt == "pote":
            conn.send(json.dumps((c.potencia(received))).encode("UTF-8"))

        elif oprt == "log":
            conn.send(json.dumps((c.log(received))).encode("UTF-8"))
        conn.close()
    
    print("cierre ciclo conexion")

s.close()






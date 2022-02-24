import socket
import re
import math as m

TCP_IP = '127.0.0.7'
TCP_PORT = 5015
BUFFER_SIZE = 1024
ENCODETYPE = "UTF-8"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.listen(5)
print ("Server Logaritmo is running...")

# ----------------------------
def doOperation(op):
    
    formC = re.compile(r'l[(](\d+)[)]')

    if formC.match(op): numero = re.search(r'(\d+)', op).group()
    else: return "Operacion no valida"

    return str(m.log(int(numero),10))
# --------------------------

adminclose = True
while adminclose:
    conn, addr = s.accept() # Direccion: addr[0], Puerto: addr[1])
    received = conn.recv(BUFFER_SIZE).decode(ENCODETYPE)

    if (received == "closeServer"):
        adminclose = False
        conn.close()

    elif received:
        conn.send(doOperation(received).encode("UTF-8"))
        conn.close()

s.close()
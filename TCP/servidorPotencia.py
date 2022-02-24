import socket

TCP_IP = '127.0.0.6'
TCP_PORT = 5014
BUFFER_SIZE = 1024
ENCODETYPE = "UTF-8"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.listen(5)
print ("Server Potenciacion is running...")

# ----------------------------

def doOperation(op):

    error = False
    error2 = 0
    num1 = ""
    num2 = ""
    set_ = True 

    for a in op:
        if(a == "^"):
            set_ = False
            error2 += 1 
        
        elif(a.isalpha()):
            error = True
            break
        
        elif(set_):
            num1 += a
        
        elif not set_:
            num2 += a
    
    if(len(num1) == 0 or len(num2) == 0 or error or error2 > 1):
        print("num: ", num1, num2)
        return "Operacion no valida"

    return str(int(num1)**int(num2))
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
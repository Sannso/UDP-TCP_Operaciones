import socket
## Python 3.7 
TCP_IP = '7A-310-4'
TCP_PORT = 6777 # > 1024 && < 65535
BUFFER_SIZE = 1024
suma=0

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.listen(5)
print ("Servidor escuchando...")

while 1:
  conn, addr = s.accept()  
  data1 = conn.recv(BUFFER_SIZE).decode("UTF-8")
  if not data1: break
  print ("Dato recibido: ", data1)
  print ("Direccion: ", addr[0])
  print ("Puerto: ", addr[1])
  conn.send("Recibido".encode("UTF-8"))

  data2 = conn.recv(BUFFER_SIZE).decode("UTF-8")
  if not data2: break
  print ("Dato recibido: ", data2)
  
  suma=int(data1) + int(data2)
  print ("Dato enviado: ", suma)
  conn.send(str(suma).encode("UTF-8"))  

  conn.close()



  

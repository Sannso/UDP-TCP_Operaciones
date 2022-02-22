import socket as skt
## Python 3.7 
TCP_IP = '192.168.213.68'
TCP_PORT = 5005 # Recomendable sea > 1024 && < 65535
BUFFER_SIZE = 1024
suma=0

s = skt.socket(skt.AF_INET, skt.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT)) # Separa un puerto en el SO
s.setsockopt(skt.SOL_SOCKET, skt.SO_REUSEADDR, 1)
s.listen(5) # Cuantos mensajes pueden quedar en cola mientras procesa
print ("Servidor escuchando...")

while 1:
  conn, addr = s.accept() 
          # Bloquea el servidor, hasta que haya una conexion 
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

  conn.close() #cierra socket



  

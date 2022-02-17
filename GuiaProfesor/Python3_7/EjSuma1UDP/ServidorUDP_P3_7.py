import socket
## Python 3.7
UDP_IP = "192.168.63.211"
UDP_PORT = 5009

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP,UDP_PORT))

print ("Servidor escuchando")
data, addr = sock.recvfrom(1024)
print ("Dato 1:", data.decode("UTF-8"), "recibido de:", addr)
sock.sendto("recibido".encode("UTF-8"),(addr[0],addr[1]))
data2, addr = sock.recvfrom(1024)
print ("Dato 2:", data2.decode("UTF-8"), "recibido de:", addr)
a = int(data.decode("UTF-8"))
b = int(data2.decode("UTF-8"))
suma = a + b
    
sock.sendto(str(suma).encode("UTF-8"),(addr[0],addr[1]))
print ("Resultado enviado: ", suma)
sock.close()

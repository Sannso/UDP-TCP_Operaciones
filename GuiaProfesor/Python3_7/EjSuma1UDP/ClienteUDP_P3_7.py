import socket
## Python 3.7

UDP_IP = "127.0.0.1"
UDP_PORT = 5009

print ("UDP TARGET IP:", UDP_IP)
print ("UDP TARGET PORT:", UDP_PORT)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

a = input("Digite numero: ")
print ("Enviando a:", a)
sock.sendto(a.encode("UTF-8"),(UDP_IP,UDP_PORT))
data = sock.recvfrom(1024)

b = input("Digite numero: ")
print ("Enviando b:", b)
sock.sendto(b.encode("UTF-8"),(UDP_IP,UDP_PORT))

suma , addr = sock.recvfrom(1024)
print ("Received message lindo, and the sum is", suma.decode("UTF-8"))
sock.close()

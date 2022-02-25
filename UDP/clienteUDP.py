from socket import *

BUFFER_SIZE = 2048
UDP_IP = "127.0.0.1"
UDP_PORT = 5009
ENCODETYPE = "UTF-8"

sock = socket(AF_INET, SOCK_DGRAM)

def checkConnection():
    connected = False

    while not connected:
        sock.sendto('CONECTADO#CLIENTE'.encode(ENCODETYPE), (UDP_IP, UDP_PORT))

        try:
            msg = sock.recv(BUFFER_SIZE)

            if msg.decode(ENCODETYPE) == 'CONECTADO':
                connected = True
                return True
        except:
            print("No se pudo establecer conexion con el servidor.")
            return False

def selectOperation():
    print("\n¿Qué operación desea a realizar?\n\n" +
        "1. Suma\n" +
        "2. Resta\n" +
        "3. Multiplicación\n" +
        "4. División\n" +
        "5. Potenciación\n" +
        "6. Logaritmación\n" +
        "7. Salir\n")
    option = int(input("Seleccione una operación: "))

    if option <= 7 and option >= 1:
        if option == 1:
            return '+'
        elif option == 2:
            return '-'
        elif option == 3:
            return '*'
        elif option == 4:
            return '/'
        elif option == 5:
            return '^'
        elif option == 6:
            return 'l'
        elif option == 7:
            return 'SALIR'
    else:
        print("\nLa opción seleccionada no es valida.")

def readNumber():
    number = 0

    while not number:
        try:
            number = input('\nPor favor, ingrese un numero: ')
            if number.isdigit():
                return number
            else:
                raise ValueError
        except:
            number = 0
            print("\nLo siento, debes ingresar un numero valido")

def main():
    while True:
        operator = selectOperation()

        if operator == 'SALIR':
            break

        # Ingresa el primer numero
        number1 = readNumber()

        if operator != 'l':
            # Ingresa el segundo numero
            number2 = readNumber()

            # Verificamos la conexion
            if checkConnection():
                # Enviamos el mensaje
                sock.sendto(f'{number1} {operator} {number2}'.encode(ENCODETYPE), (UDP_IP, UDP_PORT))
            else:
                print("\nNo se pudo establecer conexion con el servidor.")
        else:
            # Verificamos la conexion
            if checkConnection():
                # Enviamos el mensaje
                sock.sendto(f'l {number1}'.encode(ENCODETYPE), (UDP_IP, UDP_PORT))
            else:
                print("\nNo se pudo establecer conexion con el servidor.")

        # Esperamos el resultado
        msg, address = sock.recvfrom(BUFFER_SIZE)

        # Decodificamos el mensaje
        msg = msg.decode(ENCODETYPE)

        if msg == "Error":
            print("\nNo se pudo obtener el resultado. Vuelve a intentarlo.")
        elif '#' in msg:
            sock.sendto('CONECTADO'.encode(ENCODETYPE), address)
        else:
            # Imprimimos el resultado
            print(f'\nEl resultado de la operación es: {msg}')

if __name__ == "__main__":
    main()
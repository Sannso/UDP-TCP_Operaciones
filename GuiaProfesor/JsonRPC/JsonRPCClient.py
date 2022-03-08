# Call by client
from jsonrpclib import Server
def main():
    conn = Server('http://localhost:1006')
    print(conn.findlen(('a','x','d','z'), 11, {'Mt. Abu': 1602, 'Mt. Nanda': 3001,'Mt. Kirubu': 102, 'Mt.Nish': 5710}))
    print('suma: ', conn.add(5,3))
    print('resta: ', conn.substract(5,3))
    print('multiplicacion: ', conn.mul(5,3))
    print('division: ', conn.div(5,3))
if __name__ == '__main__':
    main()

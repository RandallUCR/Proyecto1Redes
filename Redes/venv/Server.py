#servidor
import socket
import threading

host = "127.0.0.1"
port = 6667

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print ("Socket Created")
sock.bind((host, port))
print ("socket bind complete")
sock.listen(1)
print ("socket now listening")


def worker(*args):
    conn = args[0]
    addr = args[1]
    try:
        print('conexion con {}.'.format(addr))

        while True:
            conn.send("server: Hello client".encode('UTF-8'))
            datos = conn.recv(4096)
            if datos:
                print('Cliente {},'.format(addr[1]) , 'dice: {}'.format(datos.decode('utf-8')))

            else:
                print("desconectado: ".format(addr[1]))
                break
    finally:
        conn.close()

while 1:
    conn, addr = sock.accept()
    threading.Thread(target=worker, args=(conn, addr)).start()
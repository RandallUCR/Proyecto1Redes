#servidor
import socket
import threading
from Configuration import listar_hashs, guardarCliente,eliminarCliente
import threading
from tkinter import *
import Configuration as c
import time

host = "192.168.0.2"
port = 6665
lista_hash = ''
tablasmaligna=[]
bandera=0
bandera2=0
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print ("Socket Created")
sock.bind((host, port))
print ("socket bind complete")
sock.listen(1)
print ("socket now listening")

datos = ''
puertoCliente = ''
puertoCli=''
idCliente = ''

def worker(*args):
    conn = args[0]
    addr = args[1]
    global lista_hash
    global datos
    global puertoCliente,idCliente,puertoCli
    global bandera , bandera2
    try:
        print('conexion con {}.'.format(addr))
        bandera = 1
        guardarCliente(addr[0],addr[1])
        puertoCli=str(addr[0])
        idCliente = str(addr[1])
        print(idCliente + puertoCli + "+++++++++++++++++++++++++")
        while True:
            conn.send("server: Hello".encode('UTF-8'))
            datos = conn.recv(4096)
            if datos:
                print('Cliente {},'.format(addr[1]) , 'dice: {}'.format(datos.decode('utf-8')))
                if(datos.decode('utf-8')== "solicitar hash"):
                    bandera2=1
                    lista_hash = listar_hashs()
                    conn.send(lista_hash.encode('UTF-8'))
                    print("Virus Encontrados por {}".format(addr[1]) +':')
                    puertoCliente= str(addr[1])
                    datos = conn.recv(4096)
                    #print("DATOOOOOS"+str(datos))
                    print("DATOS "+datos.decode('utf-8'))

            else:
                print("desconectado {}: ".format(addr[1]))

                break
    finally:
        print("Ya finalicé mi conección!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        eliminarCliente(puertoCli)
        conn.close()

def recibir():
    while 1:
        conn, addr = sock.accept()
        threading.Thread(target=worker, args=(conn, addr)).start()
        time.sleep(5)




root = Tk(className=' - Proyecto Uno Redes')
p1 = PanedWindow(root, bg='beige', orient=VERTICAL)
p1tabla = PanedWindow(p1, bg='beige', orient=VERTICAL)
p2 = PanedWindow(root, bg='beige', orient=VERTICAL)
p2tabla = PanedWindow(p2, bg='beige', orient=VERTICAL)
def interfaz():
    global datos
    root.geometry('1000x600')
    root.configure(bg='beige')

    # e = Entry(root, width = 200, borderwidth = 5)
    # e.pack()

    titulo = Label(root, text='Server', font="Verdana 20 bold", fg="black", bg='beige')
    titulo.pack(side=TOP)

    p1.pack(side=LEFT, fill=BOTH)
    titulo2 = Label(p1, text='Hashes Malignos', font="Verdana 10 bold", fg="red", bg='beige')
    titulo2.pack(side=TOP)

    p1tabla.pack(side=TOP, fill=BOTH)


    p2.pack(side=RIGHT, fill=BOTH)
    titulo3 = Label(p2, text='Clientes conectados', font="Verdana 10 bold", fg="blue", bg='beige')
    titulo3.pack(side=TOP)

    p2tabla.pack(side=TOP, fill=BOTH)

    hsh = datos
    hashes = hsh.split()
    clientes = c.listar_clientes()

    crearTabla(p1tabla, hashes,1)
    crearTabla(p2tabla, clientes,2)

    hilo2 = threading.Thread(target=hilo)
    hilo2.start()
    root.mainloop()

def crearTabla(padre,list,numero):
    if(numero==1):
        for i in range(len(list)):
            # fila= list[]
            print(str(list[i]))
            celda = Label(padre, text=list[i], font="Verdana 10 bold", fg="black", bg='beige', borderwidth=2,
                          relief='solid', width=55)
            celda.grid(row=i)
    else:
        for i in range(len(list)):
            # fila= list[]
            print(str(list[i]))
            celda = Label(padre, text=list[i], font="Verdana 10 bold", fg="black", bg='beige', borderwidth=2,
                          relief='solid', width=30)
            celda.grid(row=i)


def hilo ():
    global datos
    global tablasmaligna
    global bandera,bandera2
    hashtablas=[]
    #print("DATOS HILO"+str(datos))
    #print("PUERTO CLIENTE"+puertoCliente)
    hashtablas=sacarStringHashes()

    if(bandera==1):
        bandera=0
        hashtablas+=hashtablas
    else:
        hashtablas = hashtablas

    clientes2 = c.listar_clientes()
    if(bandera2==1):
        bandera2=0
        tablasmaligna+=hashtablas
        crearTabla(p1tabla, tablasmaligna,1)
    crearTabla(p2tabla, clientes2,2)
    time.sleep(5)
    root.after(5000, hilo())

def sacarStringHashes():
    global datos

    print("DATOS HILO" + str(datos))
    print("PUERTO CLIENTE" + puertoCliente)
    hashes2=''
    hsh2 = datos
    hashes2 = hsh2.split()
    hash3 = str(hashes2)
    final=''
    hashesFinal=[]
    print("HASH 3"+hash3)
    cont=0
    if(len(hashes2)>0):
        for i in hashes2:
            final += str(hashes2[cont]) + " detectado por: " + puertoCliente
            hashesFinal.append(final)
            cont+=1
            final=''
        print(hashesFinal)

    return hashesFinal

if __name__ == "__main__":
    eliminarCliente()
    hilo1 = threading.Thread(target=recibir)
    hilo1.start()
    hilo2 = threading.Thread(target=hilo)
    hilo2.start()
    interfaz()





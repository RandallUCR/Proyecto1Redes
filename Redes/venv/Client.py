from socket import socket
from os import scandir, getcwd
from os.path import abspath
import hashlib
import threading
import tkinter
from tkinter import ttk
import tkcalendar
import shutil
from datetime import datetime

from tkinter.filedialog import askdirectory
from tkinter.filedialog import askopenfilename
s = socket()
s.connect(("192.168.0.4", 6665))
listaHashesSer  = []

self = tkinter.Tk()

calendar = tkcalendar.Calendar()

spin1 = tkinter.Spinbox(self, values=(
    ["00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17",
     "18", "19", "20", "21", "22", "23"]), width=5, state="readonly")

spin2 = tkinter.Spinbox(self, values=(
    ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17",
     "18", "19", "20", "21", "22", "23",
     "24", "25", "26", "27", "28", "29", "30", "31", "32", "33", "34", "35", "36", "37", "38", "39", "40", "41",
     "42", "43", "44", "45", "46", "47",
     "48", "49", "50", "51", "52", "53", "54", "55", "56", "57", "58", "59"]), width=5, state="readonly")


archivos = []
lista_Programadas = []
ruta = ''

listaHashes = []
lista_archivos_a_pasar = []



def filechooser():
    global ruta
    self.directory = askdirectory( parent=self,initialdir="/",title='Por favor seleccione una carpeta')
    ruta= self.directory

def listar():
    global  ruta
    return [arch.name for arch in scandir(ruta) if arch.is_file()]


def md5():
    global archivos
    global listaHashes

    archivos=listar()

    for i in archivos:

        hash_md5 = hashlib.md5()
        with open(ruta+"\\"+i, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_md5.update(chunk)
        listaHashes.append(hash_md5.hexdigest())
    print(archivos)
    print("LISTA HASHES "+str(listaHashes))

    return listaHashes



try:
    raw_input
except NameError:
    raw_input = input


def main():
    global listaHashesSer
    global lista_archivos_a_pasar
    while True:

        input_data = s.recv(1024)

        if input_data:
            # En Python 3 recv() retorna los datos leídos
            # como un vector de bytes. Convertir a una cadena
            # en caso de ser necesario.
            print(input_data.decode("utf-8")
            if isinstance(input_data, bytes)
            else input_data)
        if (input_data.decode(("utf-8")) != "server: Hello"):
            listastr = input_data.decode(("utf-8"))
            listastr = listastr.split()
            listaHashesSer = listastr
            listaVirus=comparar()
            lista_archivos_a_pasar=listaVirus
            moverCuarentena()
            print("JJJJJJJJJJJJJJJJJJJJJJJJJJJ "+str(len(listaVirus)))
            virusEnviar=" "
            for i in listaVirus:
                virusEnviar+=' '+i

            output_data = virusEnviar
            try:
                s.send(output_data)
            except TypeError:
                s.send(bytes(output_data, "utf-8"))
            listaVirus.clear()

def comparar():
    global listaHashesSer
    global listaHashes
    print(len(listaHashesSer))
    print(len(listaHashes))
    comparacion = []

    for item in listaHashes:
        if item in listaHashesSer:
            comparacion.append(item)

    listaHashesSer.clear()
    listaHashes.clear()
    return comparacion

def moverCuarentena ():
    global archivos
    global comparacion
    global lista_archivos_a_pasar
    archivo_malo = []
    for i in archivos:
        hash_md5 = hashlib.md5()

        with open(ruta + "\\" + i, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_md5.update(chunk)
                print("mmmmmmmmmmmmmmmmm"+str(len(lista_archivos_a_pasar)))
                for item in lista_archivos_a_pasar:
                    print("mmmmmmmmmmmmmmmmm")
                    if(item == hash_md5.hexdigest()):

                        archivo_malo.append(i)
    for j in archivo_malo:
        print(j)
        shutil.move(ruta+"\\" +j, "C:\\Users\\Extreme PC}\\PycharmProjects\\Redes\\Cuarentena\\" +j)

def verificarHorasProgramadas():
    while True:
        if not (lista_Programadas is None):
            anno = datetime.now().year
            mes = datetime.now().month
            dia = datetime.now().day
            hora = datetime.now().hour
            minutos = datetime.now().minute
            fecha_Hora_actual = str(anno) + '-' + str(mes) + '-' + str(dia) + ' ' + str(hora) + ':' + str(minutos)
            for i in lista_Programadas:
                lista= []
                lista = lista_Programadas[0]
                if(fecha_Hora_actual==str(lista[1])):
                    print("ES LA HORA")
                    salir=1
                    md5()
                    lista_Programadas.remove(lista)

def Ejecutar():
   print ("Excelente")
   output_data = "solicitar hash"
   try:
       md5()
       s.send(output_data)
   except TypeError:
       s.send(bytes(output_data, "utf-8"))

def Programar():
    global fecha_Hora
    global lista_Programadas
    global ruta
    result = calendar.selection_get()
    resultHora = spin1.get()
    resultMinutos = spin2.get()
    fecha_Hora = str(result)+' '+str(resultHora)+':'+str(resultMinutos)
    ruta_fecha_hora = [ruta, fecha_Hora]
    lista_Programadas.append(ruta_fecha_hora)
    print("fecha agarrada: " + fecha_Hora)
    print("Lista:")
    for i in lista_Programadas:
        print(str(i))

def interfaz():

    self.geometry('550x350')
    self.configure(bg='beige')
    self.title('Cliente')

    botonFC = tkinter.Button(self, text="Elegir carpeta", command=filechooser)
    botonFC.grid(row=1, column=0, columnspan=1)

    boton1 = tkinter.Button(self, text="Ejecutar", command=Ejecutar)
    boton1.grid(row=1, column=3, columnspan=1)

    Label1 = tkinter.Label(self, text="Programar antivirus")
    Label1.grid(row=2, column=4, columnspan=2)

    Label2 = tkinter.Label(self, text="Fecha")
    Label2.grid(row=7, column=0, columnspan=1)

    Label3 = tkinter.Label(self, text="Hora")
    Label3.grid(row=7, column=10, columnspan=2)

    calendar = tkcalendar.Calendar()

    calendar.grid(row=8, column=3, columnspan=2)

    spin1.grid(row=7, column=12, columnspan=2)

    Label4 = tkinter.Label(self, text="Minutos")

    Label4.grid(row=7, column=15, columnspan=2)

    spin2.grid(row=7, column=18, columnspan=2)

    boton2 = tkinter.Button(self, text="Programar", command=Programar)

    boton2.grid(row=8, column=14, columnspan=2)

    self.mainloop()



if __name__ == "__main__":

    hilo2 = threading.Thread(target=main)
    hilo2.start()

    hiloProgramado = threading.Thread(target=verificarHorasProgramadas)
    hiloProgramado.start()
    interfaz()

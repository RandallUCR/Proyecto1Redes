from tkinter import *

root = Tk(className=' - Proyecto Uno Redes')
root.geometry('600x600')
root.configure(bg = 'gray')

#e = Entry(root, width = 200, borderwidth = 5)
#e.pack()

titulo = Label(root, text='Server', font = "Verdana 20 bold",fg = "white", bg = 'gray')
titulo.pack(side=TOP)
p1 = PanedWindow(root, bg = 'gray', orient=VERTICAL)
p1.pack(side=LEFT, fill=BOTH)
titulo2 = Label(p1, text='Hashes Malignos', font = "Verdana 10 bold",fg = "red", bg = 'gray')
titulo2.pack(side = TOP)
p1tabla = PanedWindow(p1, bg = 'gray', orient=VERTICAL)
p1tabla.pack(side=TOP, fill=BOTH)

p2 = PanedWindow(root, bg = 'gray', orient=VERTICAL)
p2.pack(side=RIGHT, fill=BOTH)
titulo3 = Label(p2, text='Clientes conectados', font = "Verdana 10 bold",fg = "blue", bg = 'gray')
titulo3.pack(side=TOP)
p2tabla = PanedWindow(p2, bg = 'gray', orient=VERTICAL)
p2tabla.pack(side=TOP, fill=BOTH)


hashes = ['312312312313213','09809890809','5345345345']
clientes = ['198.162.24.0','198.162.24.60','198.162.24.120']


#filas = len(list)
#cols = len(list[0])

#for i in range(filas):
    #for j in range(cols):
 #       celda = Label(p1tabla,text=list[i], font = "Verdana 10 bold",fg = "yellow", bg = 'gray', borderwidth = 2, relief = 'solid', width = 20)
  #      celda.grid(row = i)

#def click() :
#    label = Label(root, text='Hola')
#    label.pack()

#boton = Button(root, text='Hola',command= click)
#boton.pack()

def crearTabla(padre,list):
    for i in range(len(list)):
        celda = Label(padre, text=list[i], font="Verdana 10 bold", fg="white", bg='gray', borderwidth=2,
                      relief='solid', width=20)
        celda.grid(row=i)

crearTabla(p1tabla,hashes)
crearTabla(p2tabla,clientes)

root.mainloop()

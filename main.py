from tkinter import *
import tkinter as Tk
from operaciones import *

ventana = Tk()
ventana.geometry("200x200")

botonsaldo=Button(ventana,text="Consultar Saldo",command=Operaciones.saldo)
botonsaldo.pack()

botondeposito=Button(ventana,text="Depositar a cuenta",command=Operaciones.depositos)
botondeposito.pack()

botonretiro=Button(ventana,text="Retirar de la cuenta",command=Operaciones.retiro)
botonretiro.pack()

botonusuario=Button(ventana,text="Datos Usuario",command=usuario.usuario)
botonusuario.pack()

ventana.mainloop()
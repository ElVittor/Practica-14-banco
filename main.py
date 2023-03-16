from tkinter import *
from operaciones import *
import tkinter as tk
from usuarios import *

ventana = tk.Tk()
ventana.geometry("200x200")

Operaciones=Operaciones.consulasaldo()
botonsaldo=Button(ventana,text="Consultar Saldo",command=Operaciones.consulasaldo)
botonsaldo.pack()

Operaciones=Operaciones.depositos()
botondeposito=Button(ventana,text="Depositar a cuenta",command=Operaciones.depositos)
botondeposito.pack()

Operaciones=Operaciones.retiros()
botonretiro=Button(ventana,text="Retirar de la cuenta",command=Operaciones.retiros)
botonretiro.pack()

usuario=usuario.usuario()
botonusuario=Button(ventana,text="Datos Usuario",command=usuario.usuario)
botonusuario.pack()

ventana.mainloop()
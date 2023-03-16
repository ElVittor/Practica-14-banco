from usuarios import *
from tkinter import *
import tkinter as Tk
from tkinter import messagebox

class Operaciones():
    def __init__(self,saldo):
        self.saldo=saldo
        
    def depositos(self):
        ventanaoperaciones=Tk()
        
        labeldepositos=Tk.Label(ventanaoperaciones,text="Importe a depositar")
        labeldepositos.pack()
        #deposito=IntVar()
        entrydepositos=Tk.Entry(ventanaoperaciones)
        entrydepositos.pack()
        
        saldo=entrydepositos+saldo
        
        messagebox.showinfo("Nuevo Saldo","Deposito realizado con éxito. Su nuevo saldo es:"+saldo)
        
    def retiros(self):
        ventanaoperaciones=Tk()
        
        labelretiros=Tk.Label(ventanaoperaciones,text="Importe a retirar")
        labelretiros.pack()
        #retiro=IntVar()
        entryretiros=Tk.Entry(ventanaoperaciones)
        entryretiros.pack()
        
        saldo=entryretiros-saldo
        
        messagebox.showinfo("Nuevo Saldo","Retiro realizado con éxito. Su nuevo saldo es:"+saldo)
        
    def consulasaldo(self):
        saldo=saldo    
                      
        messagebox.showinfo("Nuevo Saldo","Su saldo al día de hoy es de:"+saldo)
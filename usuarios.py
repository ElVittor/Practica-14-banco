from tkinter import *

class usuario():
    def __init__(self,nombre,nocta,edad,saldo):
        self.nombre=nombre
        self.nocta=nocta
        self.edad=edad
        self.saldo=saldo
        
    def usuario(self):
        nombre="Ratón Perez"
        self.nombre.set(nombre)
        nocta=1234567890
        self.nocta.set(nocta)
        edad=45
        self.edad.set(edad)
        saldo=1000000000000
        self.saldo.set(saldo)
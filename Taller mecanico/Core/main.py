
from cProfile import label
from email.mime import image

from guizero import*
import tkinter as tk
import psycopg2
from tkinter import *

from Inicio import ingresar_admin
from Inicio import ingresar_cliente






"""
    Connect and Read: Proyecto final de la clase de Bases de Datos I
    
    @author: jazmin.maradiaga@unah.hn
    @version: 0.1.0
    @date: 2022/04/17b
    """  
    
global nombre1, nombre2,apellido1,apellido2,direccion, correo,idc
vn = tk.Tk ()
vn.title ("Formulario De registro")  
vn.geometry ("500x500")
vn.configure(background="light grey")

image = tk.PhotoImage (file = "imagenes\imagen1.gif")
image = image.subsample (1,1)
label = tk.Label (image = image)
label = tk.Label (image = image)
label.pack()    

Label (text = "Acceso al Sistema", bg = "navy", fg = "white", width = "300", height= "3", font= ("calibri", 15)).pack()

Label (text= "").pack()


boton = tk.Button (vn, text ="Iniciar como Administrador", fg = "black",width = "300", height= "3", command= ingresar_admin)
boton.pack ()
    
boton = tk.Button (vn, text ="Iniciar como cliente", fg = "black",width = "300", height= "3", command=ingresar_cliente )
boton.pack ()




vn.mainloop()
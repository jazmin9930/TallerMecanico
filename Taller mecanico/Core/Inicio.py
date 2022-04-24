

from turtle import bgcolor, left, width
import psycopg2
from guizero import*
import tkinter as tk
import psycopg2
from tkinter import *

from menu import menu_taller 
from cliene_consulta import consulta_cliente





"""
    Connect and Read: Proyecto final de la clase de Bases de Datos I
    
    @author: jazmin.maradiaga@unah.hn
    @version: 0.1.0
    @date: 2022/04/17b
    """  

def ingresar_admin ():
    global nombre1;
    global primer_apellido1;
    global segundo_apellido1;
    
    vn = tk.Tk ()
    vn.title ("Formulario De registro")  
    vn.geometry ("500x600")
    vn.configure(background="light grey")

    image = tk.PhotoImage (file = "imagenes\imagen1.gif")
    image = image.subsample (1,1)
    label = tk.Label (image = image)
    label = tk.Label (image = image)
    label.pack()    

    Label (text = "Inicio de Sesion", bg = "navy", fg = "white", width = "300", height= "3", font= ("calibri", 15)).pack()

    Label (text= "").pack()
    
    e0 = tk.Label (vn,text = "Ingrese su primer nombre",bg="gray",fg= "white")  
    e0.pack (padx = 5, pady = 5, ipadx = 5, fill= tk.X)
    nombre1= tk.Entry(vn)
    nombre1.pack (padx = 5, pady = 5, ipadx = 5, fill= tk.X)

    e = tk.Label (vn,text = "Ingrese su Primer Apellido",bg="gray",fg= "white")  
    e.pack (padx = 5, pady = 5, ipadx = 5, fill= tk.X)
    primer_apellido1= tk.Entry(vn)
    primer_apellido1.pack (padx = 5, pady = 5, ipadx = 5, fill= tk.X)

    e1 = tk.Label (vn,text = "Ingrese su Segundo apellido",bg="gray",fg= "white")  
    e1.pack (padx = 5, pady = 5, ipadx = 5, fill= tk.X)
    segundo_apellido1 = tk.Entry(vn)
    segundo_apellido1.pack (padx = 5, pady = 5, ipadx = 5, fill= tk.X)
    
    
    boton = tk.Button (vn, text ="Iniciar Sesion", fg = "black",command= validar_ingreso_admin)
    boton.pack (side = tk.LEFT)
    
    boton = tk.Button (vn, text ="Regresar", fg = "black")
    boton.pack (side = tk.LEFT)
    vn.mainloop()
    
def validar_ingreso_admin ():
    global dbConnerctor
    dbConnector=psycopg2.connect(
    host = "localhost",
    user = "postgres",
    password = "12345",
    database = "taller_Mecanico",
 )
    link2 = dbConnector.cursor()
   
    
    query = ("SELECT nombre1,apellido1,apellido2  FROM empleado WHERE nombre1 = '" +nombre1.get()+"'AND apellido1 = '"+primer_apellido1.get()+ "' AND apellido2 = '"+segundo_apellido1.get()+ "'")
    
     
    link2.execute(query)
    if link2.fetchall():
            messagebox.showinfo(message="Inicio de sesion correcto ",title="Inicio de sesion exitoso") 
            menu_taller ()
            
       
    else:
        
            messagebox.showinfo(message="Ups! Algo salio mal",title="ERROR")     





def ingresar_cliente ():
    global nombre;
    global primer_apellido;
    global segundo_apellido;
    
    vn = tk.Tk ()
    vn.title ("Formulario De registro")  
    vn.geometry ("500x600")
    vn.configure(background="light grey")

    image = tk.PhotoImage (file = "imagenes\imagen1.gif")
    image = image.subsample (1,1)
    label = tk.Label (image = image)
    label = tk.Label (image = image)
    label.pack()    

    Label (text = "Inicio de Sesion", bg = "navy", fg = "white", width = "300", height= "3", font= ("calibri", 15)).pack()

    Label (text= "").pack()  
    
    e0 = tk.Label (vn,text = "Ingrese su primer nombre",bg="gray",fg= "white")  
    e0.pack (padx = 5, pady = 5, ipadx = 5, fill= tk.X)
    nombre= tk.Entry(vn)
    nombre.pack (padx = 5, pady = 5, ipadx = 5, fill= tk.X)

    e = tk.Label (vn,text = "Ingrese su Primer Apellido",bg="gray",fg= "white")  
    e.pack (padx = 5, pady = 5, ipadx = 5, fill= tk.X)
    primer_apellido= tk.Entry(vn)
    primer_apellido.pack (padx = 5, pady = 5, ipadx = 5, fill= tk.X)

    e1 = tk.Label (vn,text = "Ingrese su Segundo apellido",bg="gray",fg= "white")  
    e1.pack (padx = 5, pady = 5, ipadx = 5, fill= tk.X)
    segundo_apellido = tk.Entry(vn)
    segundo_apellido.pack (padx = 5, pady = 5, ipadx = 5, fill= tk.X)
    
    boton = tk.Button (vn, text ="Iniciar Sesion", fg = "black",command= validar_ingreso_cliente )
    boton.pack (side = tk.LEFT)
    
    boton = tk.Button (vn, text ="Regresar", fg = "black")
    boton.pack (side = tk.LEFT)
    vn.mainloop()
    
def validar_ingreso_cliente ():
    global dbConnerctor
    dbConnector=psycopg2.connect(
    host = "localhost",
    user = "postgres",
    password = "12345",
    database = "taller_Mecanico",
 )
    link2 = dbConnector.cursor()
   
    
    query = ("SELECT nombre1,apellido1,apellido2  FROM cliente WHERE nombre1 = '" +nombre.get()+"'AND apellido1 = '"+primer_apellido.get()+ "' AND apellido2 = '"+segundo_apellido.get()+ "'")
    
     
    link2.execute(query)
    if link2.fetchall():
            messagebox.showinfo(message="Inicio de sesion correcto ",title="Inicio de sesion exitoso") 
            consulta_cliente ()
            
       
    else:
        
            messagebox.showinfo(message="Ups! Algo salio mal",title="ERROR")         


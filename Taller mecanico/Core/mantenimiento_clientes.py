
from cProfile import label
from email.mime import image
import string
from turtle import left
import psycopg2
from guizero import*
import tkinter as tk
import psycopg2
from tkinter import *

from setuptools import Command

"""
    Connect and Read: Proyecto final de la clase de Bases de Datos I
    
    @author: jazmin.maradiaga@unah.hn
    @version: 0.1.0
    @date: 2022/04/17
    """
    
    
def mantenimiento_clientes():
    global nombre1, nombre2,apellido1,apellido2, correo,idc,calle,ciudad,colonia,telefono
    
    vn = tk.Tk ()
    vn.title ("Formulario De registro")  
    vn.geometry ("500x700")
    vn.configure(background="light grey")
    
    Label (text = "Acceso al Sistema", bg = "navy", fg = "white", width = "200", height= "2", font= ("calibri", 15)).pack()
    
    
    e0 = tk.Label (vn,text = "Identificador",bg="gray",fg= "white")  
    e0.pack (padx = 5, pady = 5, ipadx = 5, fill= tk.X)
    idc= tk.Entry(vn)
    idc.pack (padx = 5, pady = 5, ipadx = 5, fill= tk.X)

    e = tk.Label (vn,text = "Primer Nombre",bg="gray",fg= "white")  
    e.pack (padx = 5, pady = 5, ipadx = 5, fill= tk.X)
    nombre1 = tk.Entry(vn)
    nombre1.pack (padx = 5, pady = 5, ipadx = 5, fill= tk.X)

    e1 = tk.Label (vn,text = "Segundo Nombre",bg="gray",fg= "white")  
    e1.pack (padx = 5, pady = 5, ipadx = 5, fill= tk.X)
    nombre2 = tk.Entry(vn)
    nombre2.pack (padx = 5, pady = 5, ipadx = 5, fill= tk.X)

    e2 = tk.Label (vn,text = "Primer Apellido",bg="gray",fg= "white")  
    e2.pack (padx = 5, pady = 5, ipadx = 5, fill= tk.X)
    apellido1 = tk.Entry(vn)
    apellido1.pack (padx = 5, pady = 5, ipadx = 5, fill= tk.X)

    e3 = tk.Label (vn,text = "Segundo Apellido",bg="gray",fg= "white")  
    e3.pack (padx = 5, pady = 5, ipadx = 5, fill= tk.X)
    apellido2= tk.Entry(vn)
    apellido2.pack (padx = 5, pady = 5, ipadx = 5, fill= tk.X)
    
    e15 = tk.Label (vn,text = "Telefono de contacto",bg="gray",fg= "white")  
    e15.pack (padx = 5, pady = 5, ipadx = 5, fill= tk.X)
    telefono= tk.Entry(vn)
    telefono.pack (padx = 5, pady = 5, ipadx = 5, fill= tk.X)

    e4 = tk.Label (vn,text = "Ingrese la Ciudad en la que vive",bg="gray",fg= "white")  
    e4.pack (padx = 5, pady = 5, ipadx = 5, fill= tk.X)
    ciudad = tk.Entry(vn)
    ciudad.pack (padx = 5, pady = 5, ipadx = 5, fill= tk.X)
    
    e4 = tk.Label (vn,text = "Ingrese la Calle",bg="gray",fg= "white")  
    e4.pack (padx = 5, pady = 5, ipadx = 5, fill= tk.X)
    calle = tk.Entry(vn)
    calle.pack (padx = 5, pady = 5, ipadx = 5, fill= tk.X)
    
    e4 = tk.Label (vn,text = "Ingrese la Colonia",bg="gray",fg= "white")  
    e4.pack (padx = 5, pady = 5, ipadx = 5, fill= tk.X)
    colonia = tk.Entry(vn)
    colonia.pack (padx = 5, pady = 5, ipadx = 5, fill= tk.X)
    
    e5 = tk.Label (vn,text = "Correo Electronico",bg="gray",fg= "white")  
    e5.pack (padx = 5, pady = 5, ipadx = 5, fill= tk.X)
    correo  = tk.Entry(vn)
    correo.pack (padx = 5, pady = 5, ipadx = 5, fill= tk.X)

    # ----- BOTONES --------
    boton = tk.Button (vn, text ="Registrar Cliente", fg = "black",command= insertar_datos)
    boton.pack (side = tk.LEFT)
    
    boton = tk.Button (vn, text ="Registrar Telefono", fg = "black",command= insertar_telefonos)
    boton.pack (side = tk.LEFT)
    
    boton = tk.Button (vn, text ="Eliminar Cliente", fg = "black", command= eliminar_cliente)
    boton.pack (side = tk.LEFT)

    boton = tk.Button (vn, text ="Actualizar Cliente", fg = "black",command=Actualizar_cliente)
    boton.pack (side = tk.LEFT)
    
    boton = tk.Button (vn, text ="Consultar Cliente", fg = "black",command=consulta_cliente)
    boton.pack (side = tk.LEFT)
    
    boton = tk.Button (vn, text ="Salir", fg = "black", command= cerrar)
    boton.pack (side = tk.LEFT)



    vn.mainloop()
 
def cerrar ():
    global vn 
    vn.destroy               
            
def insertar_datos():
    global dbConnector
        
    dbConnector=psycopg2.connect(
    host = "localhost",
    user = "postgres",
    password = "12345",
    database = "taller_Mecanico",
    )
    link2 = dbConnector.cursor()
    query = "INSERT INTO cliente (id_cliente,Nombre1,Nombre2,Apellido1,Apellido2,telefono,Ciudad,calle,colonia,correo)  VALUES ('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}','{8}','{9}') ".format(idc.get(),nombre1.get(),nombre2.get(),apellido1.get(),apellido2.get(),telefono.get(),ciudad.get(),calle.get(),colonia.get(),correo.get());
    try: 
        link2.execute(query)
        dbConnector.commit()
        
        idc.delete(0, 'end')
        nombre1.delete(0, 'end')
        nombre2.delete(0, 'end')
        apellido1.delete(0, 'end')
        apellido2.delete(0, 'end')
        telefono.delete(0, 'end')
        ciudad.delete(0, 'end')
        calle.delete(0, 'end')
        colonia.delete(0, 'end')
        correo.delete(0, 'end')
        messagebox.showinfo(message="Registro exitoso",title="Aviso" )
    except:
        dbConnector.rollback()
        messagebox.showwarning(message="Ups! Ocurrio un problema, posiblemente el usuario ya este registrado",title= "Aviso")
    
    dbConnector.close()            
    
    
def eliminar_cliente ():
    global dbConnector
        
    dbConnector=psycopg2.connect(
    host = "localhost",
    user = "postgres",
    password = "12345",
    database = "taller_Mecanico",
    )
    link2 = dbConnector.cursor()
    query = "DELETE  FROM cliente WHERE id_cliente = '" +idc.get()+"'"
    try: 
        link2.execute(query)
        dbConnector.commit()
        idc.delete(0, 'end')
        nombre1.delete(0, 'end')
        nombre2.delete(0, 'end')
        apellido1.delete(0, 'end')
        apellido2.delete(0, 'end')
        telefono.delete(0, 'end')
        ciudad.delete(0, 'end')
        calle.delete(0, 'end')
        colonia.delete(0, 'end')
        correo.delete(0, 'end')
       
        messagebox.showinfo(message="Borrado exitoso",title="Aviso" )
    except:
        dbConnector.rollback()
        messagebox.showwarning(message="Ups! Ocurrio un problema",title= "Aviso")
    
    dbConnector.close()    
    
def Actualizar_cliente ():
    global dbConnector
        
    dbConnector=psycopg2.connect(
    host = "localhost",
    user = "postgres",
    password = "12345",
    database = "taller_Mecanico",
    )
    link2 = dbConnector.cursor()
    #nombre1.get(),nombre2.get(),apellido1.get(),apellido2.get(),direccion.get(),correo.get()
    query = "UPDATE cliente SET Nombre1 = '"+nombre1.get()+"',Nombre2 = '"+nombre2.get()+"',apellido1 = '"+apellido1.get()+"',apellido2= '"+apellido2.get()+"',correo='"+correo.get()+"' WHERE id_cliente='"+idc.get()+"'"
    try: 
        link2.execute(query)
        dbConnector.commit()
        idc.delete(0, 'end')
        nombre1.delete(0, 'end')
        nombre2.delete(0, 'end')
        apellido1.delete(0, 'end')
        apellido2.delete(0, 'end')
        telefono.delete(0, 'end')
        ciudad.delete(0, 'end')
        calle.delete(0, 'end')
        colonia.delete(0, 'end')
        correo.delete(0, 'end')
       
        messagebox.showinfo(message="Actualizado exitoso",title="Aviso" )
    except:
        dbConnector.rollback()
        messagebox.showwarning(message="Ups! Ocurrio un problema",title= "Aviso")
    
    dbConnector.close()    
    
def consulta_cliente():
    if (idc.get() == ""):
        messagebox.showinfo(message="Obteniendo Consulta",title="Aviso" )
    else:     
       global dbConnector
        
       dbConnector=psycopg2.connect(
       host = "localhost",
       user = "postgres",
       password = "12345",
       database = "taller_Mecanico",
       )
       link2 = dbConnector.cursor()  
       query = "SELECT * FROM cliente WHERE id_cliente = '"+idc.get()+"'"
       link2.execute(query)
       
       
       #idc.delete(0, 'end')
       nombre1.delete(0, 'end')
       nombre2.delete(0, 'end')
       apellido1.delete(0, 'end')
       apellido2.delete(0, 'end')
       telefono.delete(0, 'end')
       ciudad.delete(0, 'end')
       calle.delete(0, 'end')
       colonia.delete(0, 'end')
       correo.delete(0, 'end')
       
       result = link2.fetchall()
       
       for item in result:
           nombre1.insert(0,item[1])
           nombre2.insert(0,item[2])
           apellido1.insert(0,item[3])
           apellido2.insert(0,item[4])
           telefono.insert(0,item[5])
           ciudad.insert(0,item[6])
           calle.insert(0,item[7])
           colonia.insert(0,item[8])
           correo.insert(0,item[9])
       
       dbConnector.close()      


def insertar_telefonos ():
    global dbConnector
        
    dbConnector=psycopg2.connect(
    host = "localhost",
    user = "postgres",
    password = "12345",
    database = "taller_Mecanico",
    )
    link2 = dbConnector.cursor()
    query = "INSERT INTO telefonos (id_cliente,telefono)  VALUES ('{0}','{1}') ".format(idc.get(),telefono.get());
    try: 
        link2.execute(query)
        dbConnector.commit()
        
        idc.delete(0, 'end')
       
        telefono.delete(0, 'end')
        
        messagebox.showinfo(message="Registro exitoso",title="Aviso" )
    except:
        dbConnector.rollback()
        messagebox.showwarning(message="Ups! Ocurrio un problema, posiblemente el usuario ya este registrado",title= "Aviso")
    
    dbConnector.close()            



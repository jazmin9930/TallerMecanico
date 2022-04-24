from cProfile import label

import psycopg2
from guizero import*
import tkinter as tk
import psycopg2
from tkinter import *
from mantenimiento_clientes import mantenimiento_clientes






"""
    Connect and Read: Proyecto final de la clase de Bases de Datos I
    
    @author: jazmin.maradiaga@unah.hn
    @version: 0.1.0
    @date: 2022/04/17b
    """  
    
def admin_vehiculos ():
    global placa,idc,modelo,motor
    vn = tk.Tk ()
    vn.title (" Folmurario de Vehiculos")  
    vn.geometry ("500x600")
    vn.configure(background="light grey")
    
    image = tk.PhotoImage (file = "imagenes\imagen1.gif")
    image = image.subsample (1,1)
    label = tk.Label (image = image)
    label = tk.Label (image = image)
    label.pack() 
     

    Label (text = "Vehiculos", bg = "navy", fg = "white", width = "200", height= "2", font= ("calibri", 15)).pack()
    
    e9 = tk.Label (vn,text = "Placa del Vehiculo",bg="gray",fg= "white")  
    e9.pack (padx = 5, pady = 5, ipadx = 5, fill= tk.X)
    placa= tk.Entry(vn)
    placa.pack (padx = 5, pady = 5, ipadx = 5, fill= tk.X)
    
    e = tk.Label (vn,text = "Identificador del Cliente",bg="gray",fg= "white")  
    e.pack (padx = 5, pady = 5, ipadx = 5, fill= tk.X)
    idc = tk.Entry(vn)
    idc.pack (padx = 5, pady = 5, ipadx = 5, fill= tk.X)
    
    e = tk.Label (vn,text = "Modelo del Vehiculo",bg="gray",fg= "white")  
    e.pack (padx = 5, pady = 5, ipadx = 5, fill= tk.X)
    modelo = tk.Entry(vn)
    modelo.pack (padx = 5, pady = 5, ipadx = 5, fill= tk.X)

    e2 = tk.Label (vn,text = "Numero del Motor",bg="gray",fg= "white")  
    e2.pack (padx = 5, pady = 5, ipadx = 5, fill= tk.X)
    motor = tk.Entry(vn)
    motor.pack (padx = 5, pady = 5, ipadx = 5, fill= tk.X)

    
    
    boton = tk.Button (vn, text ="Registrar Vehiculo", fg = "black",command=insertar_vehiculo)
    boton.pack (side = tk.LEFT)
    
    boton = tk.Button (vn, text ="Consultar Vehiculo", fg = "black",command=consultar_vehiculo)
    boton.pack (side = tk.LEFT)
    
    boton = tk.Button (vn, text ="Actualizar Vehiculo", fg = "black",command=actualizar_vehiculo)
    boton.pack (side = tk.LEFT)
    
    boton = tk.Button (vn, text ="Eliminar Vehiculo", fg = "black",command=eliminar_vehiculo)
    boton.pack (side = tk.LEFT)
    
    
    vn.mainloop()   
    
def insertar_vehiculo():
    global dbConnector
        
    dbConnector=psycopg2.connect(
    host = "localhost",
    user = "postgres",
    password = "12345",
    database = "taller_Mecanico",
    )
    link2 = dbConnector.cursor()
    query = "INSERT INTO vehiculo (placa,id_cliente,modelo,numero_motor)  VALUES ('{0}','{1}','{2}','{3}') ".format(placa.get(),idc.get(),modelo.get(),motor.get());
    try: 
        link2.execute(query)
        dbConnector.commit()
        
        placa.delete(0, 'end')
        idc.delete(0, 'end')
        modelo.delete(0, 'end')
        motor.delete(0, 'end')
        
        messagebox.showinfo(message="Registro exitoso",title="Aviso" )
    except:
        dbConnector.rollback()
        messagebox.showwarning(message="Ups! Ocurrio un problema, posiblemente el usuario ya este registrado",title= "Aviso")
    
    dbConnector.close()    
    
    
def eliminar_vehiculo():
    global dbConnector
        
    dbConnector=psycopg2.connect(
    host = "localhost",
    user = "postgres",
    password = "12345",
    database = "taller_Mecanico",
    )
    link2 = dbConnector.cursor()
    query = "DELETE  FROM vehiculo WHERE placa = '" +placa.get()+"'"
    try: 
        link2.execute(query)
        dbConnector.commit()
        placa.delete(0, 'end')
        idc.delete(0, 'end')
        modelo.delete(0, 'end')
        motor.delete(0, 'end')
        
        messagebox.showinfo(message="Borrado exitoso",title="Aviso" )
    except:
        dbConnector.rollback()
        messagebox.showwarning(message="Ups! Ocurrio un problema",title= "Aviso")
    
    dbConnector.close()     
    
def actualizar_vehiculo ():
    global dbConnector
        
    dbConnector=psycopg2.connect(
    host = "localhost",
    user = "postgres",
    password = "12345",
    database = "taller_Mecanico",
    )
    link2 = dbConnector.cursor()
    #nombre1.get(),nombre2.get(),apellido1.get(),apellido2.get(),direccion.get(),correo.get()
    query = "UPDATE vehiculo SET placa = '"+placa.get()+"',id_cliente = '"+idc.get()+"',modelo = '"+modelo.get()+"',numero_motor= '"+motor.get()+"' WHERE placa='"+placa.get()+"'"
    try: 
        link2.execute(query)
        dbConnector.commit()
        
        placa.delete(0, 'end')
        idc.delete(0, 'end')
        modelo.delete(0, 'end')
        motor.delete(0, 'end')
        
        
       
        messagebox.showinfo(message="Actualizado exitoso",title="Aviso" )
    except:
        dbConnector.rollback()
        messagebox.showwarning(message="Ups! Ocurrio un problema",title= "Aviso")
    
    dbConnector.close()    
    
def consultar_vehiculo ():
    if (placa.get() == ""):
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
       query = "SELECT * FROM vehiculo WHERE placa = '"+placa.get()+"'"
       link2.execute(query)
       
       placa.delete(0, 'end')
       idc.delete(0, 'end')
       modelo.delete(0, 'end')
       motor.delete(0, 'end')
       
       
       result = link2.fetchall()
       
       for item in result:
           placa.insert(0,item[0])
           idc.insert(0,item[1])
           modelo.insert(0,item[2])
           motor.insert(0,item[3])
       
       dbConnector.close()  
         
#admin_vehiculos ()
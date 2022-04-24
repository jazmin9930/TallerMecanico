from cProfile import label
from email.mime import image

import psycopg2
from guizero import*
import tkinter as tk
import psycopg2
from tkinter import *






"""
    Connect and Read: Proyecto final de la clase de Bases de Datos I
    
    @author: jazmin.maradiaga@unah.hn
    @version: 0.1.0
    @date: 2022/04/17b
    """  
    
def admin_vehiculos ():
    global estado, placa
    vn = tk.Tk ()
    vn.title ("Estado del Vehiculo")  
    vn.geometry ("500x500")
    vn.configure(background="light grey")
    
    image = tk.PhotoImage (file = "imagenes\imagen1.gif")
    image = image.subsample (1,1)
    label = tk.Label (image = image)
    label = tk.Label (image = image)
    label.pack() 
     

    Label (text = "Estado del Vehiculo", bg = "navy", fg = "white", width = "200", height= "2", font= ("calibri", 15)).pack()
    
    e9 = tk.Label (vn,text = "Ingrese la Placa del Vehiculo",bg="gray",fg= "white")  
    e9.pack (padx = 5, pady = 5, ipadx = 5, fill= tk.X)
    placa= tk.Entry(vn)
    placa.pack (padx = 5, pady = 5, ipadx = 5, fill= tk.X)
    
    e = tk.Label (vn,text = "Estado del Vehiculo",bg="gray",fg= "white")  
    e.pack (padx = 5, pady = 5, ipadx = 5, fill= tk.X)
    estado = tk.Entry(vn)
    estado.pack (padx = 5, pady = 5, ipadx = 5, fill= tk.X)
    
    boton = tk.Button (vn, text ="Consultar Vehiculo", fg = "black",command= consultar_vehiculo )
    boton.pack (side = tk.LEFT)
    
    boton = tk.Button (vn, text ="Actualizar Vehiculo", fg = "black", command=actualizar_estado)
    boton.pack (side = tk.LEFT)
    
    
   
    vn.mainloop()    


    

def actualizar_estado():
    global dbConnector
        
    dbConnector=psycopg2.connect(
    host = "localhost",
    user = "postgres",
    password = "12345",
    database = "taller_Mecanico",
    )
    link2 = dbConnector.cursor()
    #nombre1.get(),nombre2.get(),apellido1.get(),apellido2.get(),direccion.get(),correo.get()
    query = "UPDATE cita SET estado = '"+estado.get()+"' WHERE placa_carro='"+placa.get()+"'"
    try: 
        link2.execute(query)
        dbConnector.commit()
        
        placa.delete(0, 'end')
        estado.delete(0, 'end')
        
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
       query = "SELECT * FROM cita WHERE placa_carro = '"+placa.get()+"'"
       link2.execute(query)
       
       placa.delete(0, 'end')
       estado.delete(0, 'end')
       
       result = link2.fetchall()
       
       for item in result:
           
           placa.insert(0,item[9])
           estado.insert(0,item[10])
           
           
           
       dbConnector.close()      
       
#admin_vehiculos ()      
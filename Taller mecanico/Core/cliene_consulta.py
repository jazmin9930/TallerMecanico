from cProfile import label

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
    
def consulta_cliente ():
    global estado, placa,idc,nombre1,apellido1,apellido2,telefono,cita
    
    vn = tk.Tk ()
    vn.title ("Rastreo de Cita")  
    vn.geometry ("500x500")
    vn.configure(background="light grey")
    
    image = tk.PhotoImage (file = "imagenes\imagen1.gif")
    image = image.subsample (1,1)
    label = tk.Label (image = image)
    label = tk.Label (image = image)
    label.pack()    
    
    
     
     

    Label (text = "Estado del Vehiculo", bg = "navy", fg = "white", width = "200", height= "2", font= ("calibri", 15)).pack()
    
    e9 = tk.Label (vn,text = "Ingrese el Numero de Cita",bg="gray",fg= "white")  
    e9.pack (padx = 5, pady = 5, ipadx = 5, fill= tk.X)
    cita= tk.Entry(vn)
    cita.pack (padx = 5, pady = 5, ipadx = 5, fill= tk.X)
    
    e9 = tk.Label (vn,text = "Estado del Vehiculo",bg="gray",fg= "white")  
    e9.pack (padx = 5, pady = 5, ipadx = 5, fill= tk.X)
    
    
    estado= tk.Entry(vn)
    estado.pack (padx = 5, pady = 5, ipadx = 5, fill= tk.X)
    
    e9 = tk.Label (vn,text = "Datos del cliente",bg="gray",fg= "white")  
    e9.pack (padx = 5, pady = 5, ipadx = 5, fill= tk.X)
    
    placa= tk.Entry(vn)
    placa.pack (padx = 5, pady = 5, ipadx = 5, fill= tk.X)
    
    idc= tk.Entry(vn)
    idc.pack (padx = 5, pady = 5, ipadx = 5, fill= tk.X)
    
    nombre1= tk.Entry(vn)
    nombre1.pack (padx = 5, pady = 5, ipadx = 5, fill= tk.X)
    
    apellido1= tk.Entry(vn)
    apellido1.pack (padx = 5, pady = 5, ipadx = 5, fill= tk.X)
    
    apellido2= tk.Entry(vn)
    apellido2.pack (padx = 5, pady = 5, ipadx = 5, fill= tk.X)
    
    telefono= tk.Entry(vn)
    telefono.pack (padx = 5, pady = 5, ipadx = 5, fill= tk.X)
    
   
    boton = tk.Button (vn, text ="Consultar Vehiculo", fg = "black",command=consultar_vehiculo )
    boton.pack (side = tk.LEFT)
    
    
    
    
    
    
   
    vn.mainloop()    
  
def consultar_vehiculo ():
    if (cita.get() == ""):
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
       query = "SELECT * FROM cita WHERE id_cita = '"+cita.get()+"'"
       link2.execute(query)
       
       placa.delete(0, 'end')
       nombre1.delete(0, 'end')
       apellido1.delete(0, 'end')
       apellido2.delete(0, 'end')
       telefono.delete(0, 'end')
       estado.delete(0, 'end')
       idc.delete(0, 'end')
       
       result = link2.fetchall()
       
       for item in result:
           
           
           
           idc.insert(0,item[1])
           nombre1.insert(0,item[2])
           apellido1.insert(0,item[3])
           apellido2.insert(0,item[4])
           telefono.insert(0,item[5])
           placa.insert(0,item[9])
           estado.insert(0,item[10])
            
           
           
           
       dbConnector.close()        
       
#consulta_cliente ()       
        
    
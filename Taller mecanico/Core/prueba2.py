from cProfile import label
from email.mime import image
import string
from turtle import bgcolor, left, width
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

def realizar_cita ():
    global nombre1,apellido1,apellido2,telefono,fecha,Hora,servicio,placa,estado,idc,idcita
    vn = tk.Tk ()
    vn.title ("Formulario De registro De Cita")  
    vn.geometry ("500x700")
    vn.configure(background="light grey")

    #Label (text = "Agendar Cita", bg = "navy", fg = "white", width = "200", height= "2", font= ("calibri", 15)).pack()
    
    
    e9 = tk.Label (vn,text = "Identificador de la Cita",bg="gray",fg= "white")  
    e9.pack (padx = 5, pady = 5, ipadx = 5, fill= tk.X)
    idcita= tk.Entry(vn)
    idcita.pack (padx = 5, pady = 5, ipadx = 5, fill= tk.X)
    
    e0 = tk.Label (vn,text = "Identificador del Cliente",bg="gray",fg= "white")  
    e0.pack (padx = 5, pady = 5, ipadx = 5, fill= tk.X)
    idc= tk.Entry(vn)
    idc.pack (padx = 5, pady = 5, ipadx = 5, fill= tk.X)

    e = tk.Label (vn,text = "Primer Nombre",bg="gray",fg= "white")  
    e.pack (padx = 5, pady = 5, ipadx = 5, fill= tk.X)
    nombre1 = tk.Entry(vn)
    nombre1.pack (padx = 5, pady = 5, ipadx = 5, fill= tk.X)

    e2 = tk.Label (vn,text = "Primer Apellido",bg="gray",fg= "white")  
    e2.pack (padx = 5, pady = 5, ipadx = 5, fill= tk.X)
    apellido1 = tk.Entry(vn)
    apellido1.pack (padx = 5, pady = 5, ipadx = 5, fill= tk.X)

    e3 = tk.Label (vn,text = "Segundo Apellido",bg="gray",fg= "white")  
    e3.pack (padx = 5, pady = 5, ipadx = 5, fill= tk.X)
    apellido2= tk.Entry(vn)
    apellido2.pack (padx = 5, pady = 5, ipadx = 5, fill= tk.X)

    e4 = tk.Label (vn,text = "Telefono de Contacto",bg="gray",fg= "white")  
    e4.pack (padx = 5, pady = 5, ipadx = 5, fill= tk.X)
    telefono = tk.Entry(vn)
    telefono.pack (padx = 5, pady = 5, ipadx = 5, fill= tk.X)

    e5 = tk.Label (vn,text = "Fecha de Entrada",bg="gray",fg= "white")  
    e5.pack (padx = 5, pady = 5, ipadx = 5, fill= tk.X)
    fecha  = tk.Entry(vn)
    fecha.pack (padx = 5, pady = 5, ipadx = 5, fill= tk.X)
    
    var=tk.StringVar(vn)
    var.set('Horario')
    opciones=['7:00:00 ','8:00:00 ', '9:00:00 ', '10:00:00 ', '11:00:00 ', '12:00:00 ', '13:00:00 ','14:00:00','15:0000']
    opcion = tk.OptionMenu(vn,var,*opciones)
    #opcion.config(width=20)
    opcion.pack()
    Hora=tk.Text(vn, bg='white', textvariable=var,padx=5,pady=5,width=50)
    Hora.pack(padx = 5, pady = 5, ipadx = 5, fill= tk.X)
    
    e7 = tk.Label (vn,text = "Tipo de Servicio",bg="gray",fg= "white")  
    e7.pack (padx = 5, pady = 5, ipadx = 5, fill= tk.X)
    servicio  = tk.Entry(vn)
    servicio.pack (padx = 5, pady = 5, ipadx = 5, fill= tk.X)
    
    e8 = tk.Label (vn,text = "Ingrese la Placa del Vehiculo",bg="gray",fg= "white")  
    e8.pack (padx = 5, pady = 5, ipadx = 5, fill= tk.X)
    placa  = tk.Entry(vn)
    placa.pack (padx = 5, pady = 5, ipadx = 5, fill= tk.X)
    
    e7 = tk.Label (vn,text = "Estado del Vehiculo",bg="gray",fg= "white")  
    e7.pack (padx = 5, pady = 5, ipadx = 5, fill= tk.X)
    estado  = tk.Entry(vn)
    estado.pack (padx = 5, pady = 5, ipadx = 5, fill= tk.X)

    # ----- BOTONES --------
    boton = tk.Button (vn, text ="Ingresar Cita", fg = "black", command=insertar_datos)
    boton.pack (side = tk.LEFT)
    
    boton = tk.Button (vn, text ="Consultar Cita", fg = "black", command=consultar_cita)
    boton.pack (side = tk.LEFT)
    
    boton = tk.Button (vn, text ="Registrar Cliente", fg = "black", command= mantenimiento_clientes)
    boton.pack (side = tk.LEFT)
    
   
    
    boton = tk.Button (vn, text ="Regresar al menu", fg = "black")
    boton.pack (side = tk.LEFT)

    
    
    vn.mainloop()
    
def insertar_datos():
    global dbConnector
        
    dbConnector=psycopg2.connect(
    host = "localhost",
    user = "postgres",
    password = "12345",
    database = "taller_Mecanico",
    )
    link2 = dbConnector.cursor()
    query = "INSERT INTO cita (id_cita,id_cliente,nombre_cliente,Primer_apellido,segundo_apellido,telefono,fecha_entrada,hora_entrada,tipo_servicio,placa_carro,estado)  VALUES ('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}','{8}','{9}','{10}') ".format(idcita.get(),idc.get(),nombre1.get(),apellido1.get(),apellido2.get(),telefono.get(),fecha.get(),Hora.get(),servicio.get(),placa.get(),estado.get());
    try: 
        link2.execute(query)
        dbConnector.commit()
        
        idcita.delete(0, 'end')
        idc.delete(0, 'end')
        nombre1.delete(0, 'end')
        apellido1.delete(0, 'end')
        apellido2.delete(0, 'end')
        telefono.delete(0, 'end')
        fecha.delete(0, 'end')
        Hora.delete(0, 'end')
        servicio.delete(0, 'end')
        placa.delete(0, 'end')
        estado.delete(0, 'end')
        messagebox.showinfo(message="Registro exitoso",title="Aviso" )
    except:
        dbConnector.rollback()
        messagebox.showwarning(message="Ups! Ocurrio un problema, posiblemente el usuario ya este registrado",title= "Aviso")
    
    dbConnector.close()            
    
def consultar_cita(): 
        
    global dbConnector
        
    dbConnector=psycopg2.connect(
    host = "localhost",
    user = "postgres",
    password = "12345",
    database = "taller_Mecanico",
    )
    link2 = dbConnector.cursor()  
    query = "SELECT * FROM cliente WHERE id_cliente = '"+idc.get()+"'"
    
    try: 
        link2.execute(query)
       
       
        idc.delete(0, 'end')
        nombre1.delete(0, 'end')
        apellido1.delete(0, 'end')
        apellido2.delete(0, 'end')
        telefono.delete(0, 'end')
       
       
        result = link2.fetchall()
       
        for item in result:
            idc.insert(0,item[0])
            nombre1.insert(0,item[1])
            apellido1.insert(0,item[3])
            apellido2.insert(0,item[4])
            telefono.insert(0,item[5])
    except:
        dbConnector.rollback()
        messagebox.showwarning(message="Cliente no Registrado",title= "Aviso")
    
    dbConnector.close()         
       
             
      
        
realizar_cita ()
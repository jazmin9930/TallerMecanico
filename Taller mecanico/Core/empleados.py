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
    @date: 2022/04/17
    """  


def registrar_empleado ():
    global idempleado,nombre1,apellido1,apellido2,telefono,puesto,asesor, nombre2
    vn = tk.Tk ()
    vn.title ("Formulario De registro De Empleados")  
    vn.geometry ("500x700")
    vn.configure(background="light grey")
     

    Label (text = "Registrar Empleado", bg = "navy", fg = "white", width = "200", height= "2", font= ("calibri", 15)).pack()
    
    e9 = tk.Label (vn,text = "Identificador del Empleado",bg="gray",fg= "white")  
    e9.pack (padx = 5, pady = 5, ipadx = 5, fill= tk.X)
    idempleado= tk.Entry(vn)
    idempleado.pack (padx = 5, pady = 5, ipadx = 5, fill= tk.X)
    
    e = tk.Label (vn,text = "Primer Nombre",bg="gray",fg= "white")  
    e.pack (padx = 5, pady = 5, ipadx = 5, fill= tk.X)
    nombre1 = tk.Entry(vn)
    nombre1.pack (padx = 5, pady = 5, ipadx = 5, fill= tk.X)
    
    e = tk.Label (vn,text = "Segundo Nombre",bg="gray",fg= "white")  
    e.pack (padx = 5, pady = 5, ipadx = 5, fill= tk.X)
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

    e4 = tk.Label (vn,text = "Telefono de Contacto",bg="gray",fg= "white")  
    e4.pack (padx = 5, pady = 5, ipadx = 5, fill= tk.X)
    telefono = tk.Entry(vn)
    telefono.pack (padx = 5, pady = 5, ipadx = 5, fill= tk.X)

    e5 = tk.Label (vn,text = "Tipo de puesto",bg="gray",fg= "white")  
    e5.pack (padx = 5, pady = 5, ipadx = 5, fill= tk.X)
    puesto  = tk.Entry(vn)
    puesto.pack (padx = 5, pady = 5, ipadx = 5, fill= tk.X)
    
    e6 = tk.Label (vn,text = "Ingrese el ID de Asesor",bg="gray",fg= "white")  
    e6.pack (padx = 5, pady = 5, ipadx = 5, fill= tk.X)
    asesor  = tk.Entry(vn)
    asesor.pack (padx = 5, pady = 5, ipadx = 5, fill= tk.X)
    
    boton = tk.Button (vn, text ="Registrar Empleado", fg = "black",command= registrar_empleado)
    boton.pack (side = tk.LEFT)
    
    boton = tk.Button (vn, text ="Consultar Empleado", fg = "black", command= consultar_empleado)
    boton.pack (side = tk.LEFT)
    
    boton = tk.Button (vn, text ="Actualizar empleado", fg = "black", command= actualizar_empleado)
    boton.pack (side = tk.LEFT)
    
    boton = tk.Button (vn, text ="Eliminar Empleado", fg = "black")
    boton.pack (side = tk.LEFT)
    
    
    vn.mainloop()
    
def insertar_empleado ():
    global dbConnerctor
    dbConnector=psycopg2.connect(
    host = "localhost",
    user = "postgres",
    password = "12345",
    database = "taller_Mecanico",
    )
    link2 = dbConnector.cursor()
    query = "INSERT INTO empleado (id_empleado,nombre1,nombre2,apellido1,apellido2,telefono,tipo,id_empleado_asesor)  VALUES ('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}') ".format(idempleado.get(),nombre1.get(),nombre2.get(),apellido1.get(),apellido2.get(),telefono.get(),puesto.get(),asesor.get());
    try: 
        link2.execute(query)
        dbConnector.commit()
        
        idempleado.delete(0, 'end')
        nombre1.delete(0, 'end')
        nombre2.delete(0, 'end')
        apellido1.delete(0, 'end')
        apellido2.delete(0, 'end')
        telefono.delete(0, 'end')
        puesto.delete(0, 'end')
        asesor.delete(0, 'end')
        
        messagebox.showinfo(message="Registro exitoso",title="Aviso" )
    except:
        dbConnector.rollback()
        messagebox.showwarning(message="Ups! Ocurrio un problema, posiblemente el usuario ya este registrado",title= "Aviso")
    
    dbConnector.close()    
    

def actualizar_empleado():
    dbConnector=psycopg2.connect(
    host = "localhost",
    user = "postgres",
    password = "12345",
    database = "taller_Mecanico",
    )
    link2 = dbConnector.cursor()
    #nombre1.get(),nombre2.get(),apellido1.get(),apellido2.get(),direccion.get(),correo.get()
    query = "UPDATE empleado SET id_empleado = '"+idempleado.get()+"',nombre1 = '"+nombre1.get()+"',nombre2 = '"+nombre2.get()+"',apellido1= '"+apellido1.get()+"',apellido2='"+apellido2.get()+"', telefono = '"+telefono.get()+"' ,tipo = '"+puesto.get()+"',id_empleado_asesor = '"+asesor.get()+"' WHERE id_empleado='"+idempleado.get()+"'"
    try: 
        link2.execute(query)
        dbConnector.commit()
        idempleado.delete(0, 'end')
        nombre1.delete(0, 'end')
        nombre2.delete(0, 'end')
        apellido1.delete(0, 'end')
        apellido2.delete(0, 'end')
        telefono.delete(0, 'end')
        puesto.delete(0, 'end')
        asesor.delete(0, 'end')
        
       
        messagebox.showinfo(message="Actualizado exitoso",title="Aviso" )
    except:
        dbConnector.rollback()
        messagebox.showwarning(message="Ups! Ocurrio un problema",title= "Aviso")
    
    dbConnector.close()   
    
def consultar_empleado():
    global dbConnector
        
    dbConnector=psycopg2.connect(
    host = "localhost",
    user = "postgres",
    password = "12345",
    database = "taller_Mecanico",
    )
    link2 = dbConnector.cursor()  
    query = "SELECT * FROM empleado WHERE id_empleado = '"+idempleado.get()+"'"
    
    try: 
        link2.execute(query)
       
       
        idempleado.delete(0, 'end')
        nombre1.delete(0, 'end')
        nombre2.delete(0, 'end')
        apellido1.delete(0, 'end')
        apellido2.delete(0, 'end')
        telefono.delete(0, 'end')
        puesto.delete(0, 'end')
        asesor.delete(0, 'end')
       
       
        result = link2.fetchall()
       
        for item in result:
            idempleado.insert(0,item[0])
            nombre1.insert(0,item[1])
            nombre2.insert(0,item[2])
            apellido1.insert(0,item[3])
            apellido2.insert(0,item[4])
            telefono.insert(0,item[5])
            puesto.insert(0,item[6])
            asesor.insert(0,item[7])
    except:
        dbConnector.rollback()
        messagebox.showwarning(message="Cliente no Registrado",title= "Aviso")
    
    dbConnector.close()            
        
        
      
    
  
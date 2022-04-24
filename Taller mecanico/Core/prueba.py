from cProfile import label
from email.mime import image
import string
from turtle import bgcolor, color, left, width
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
    
    popup = Menu(vn, tearoff=0)
    popup.add_command(label="7:00 am", command= hora_7) # , command=next) etc...
    popup.add_command(label="8: 00 am", command=hora_7)
    popup.add_separator()
    popup.add_command(label="9:00 am", command=hora_7)
     

    Label (text = "Estado del Vehiculo", bg = "navy", fg = "white", width = "200", height= "2", font= ("calibri", 15)).pack()   
    
    barraMenu= Menu(vn)
    menuHora= Menu (barraMenu)
    menuHora.add_command(label="7:00 am")
    menuHora.add_command(label="8:00 am")
    menuHora.add_command(label="9:00 am")
    menuHora.add_command(label="10:00 am")
    menuHora.add_command(label="11:00 am")
    menuHora.add_command(label="12:00 pm")
    menuHora.add_command(label="1:00 pm")
    menuHora.add_command(label="2:00 pm")
    menuHora.add_command(label="3:00 pm")
    
    barraMenu.add_cascade(label="Horario",menu= menuHora)
    vn.config(menu=barraMenu)
    
    
    var=tk.StringVar(vn)
    var.set('Horario')
    opciones=['7:00 ','8:00 ', '9:00 ', '10:00 ', '11:00 ', '12:00 ', '13:00 ','14:00','15:00']
    opcion = tk.OptionMenu(vn,var,*opciones)
    #opcion.config(width=20)
    opcion.pack()
    color=tk.Label(vn, bg='plum', textvariable=var,padx=5,pady=5,width=50)
    color.pack()
    
    
    
    
    

    vn.mainloop()  
    
def hora_7():
    global dbConnector
        
    dbConnector=psycopg2.connect(
    host = "localhost",
    user = "postgres",
    password = "12345",
    database = "taller_Mecanico",
    )
    link2 = dbConnector.cursor()
    query = "INSERT INTO horaFecha (hora,fecha)  VALUES ('7:00 am ', current_date) "
    try: 
        link2.execute(query)
        dbConnector.commit()
        
       
        
        messagebox.showinfo(message="Registro exitoso",title="Aviso" )
    except:
        dbConnector.rollback()
        messagebox.showwarning(message="Ups! Ocurrio un problema, posiblemente el usuario ya este registrado",title= "Aviso")
    
    dbConnector.close()
    
def hora_8():
    global dbConnector
        
    dbConnector=psycopg2.connect(
    host = "localhost",
    user = "postgres",
    password = "12345",
    database = "taller_Mecanico",
    )
    link2 = dbConnector.cursor()
    query = "INSERT INTO horaFecha (hora,fecha)  VALUES ('8:00 am ', current_date) "
    try: 
        link2.execute(query)
        dbConnector.commit()
        
       
        
        messagebox.showinfo(message="Registro exitoso",title="Aviso" )
    except:
        dbConnector.rollback()
        messagebox.showwarning(message="Ups! Ocurrio un problema, posiblemente el usuario ya este registrado",title= "Aviso")
    
    dbConnector.close()    
    
admin_vehiculos () 
    
    
           
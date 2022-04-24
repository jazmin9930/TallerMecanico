
from guizero import*

from mantenimiento_clientes import mantenimiento_clientes
from Vehiculos import admin_vehiculos
from realizar_cita import realizar_cita
from empleados import registrar_empleado
from admin_vehiculos import admin_vehiculos

"""
    Connect and Read: Proyecto final de la clase de Bases de Datos I
    
    @author: jazmin.maradiaga@unah.hn
    @version: 0.1.0
    @date: 2022/04/17
    """
    
def menu_taller ():
 app = App(title="Empleado")
 top_text = Text(app, text="Bienvenido", bg = "navy",height="3",width="300",align="top")
 top_text.text_color = "white"
 picture = Picture(app, image="imagenes/imagen1.ico",width=300, height=200)
 top_text = Text(app, text="Elija cualquier accion a ejecutar", bg = "navy",height="3",width="300",align="top")
 top_text.text_color = "white"

 button = PushButton(app,text="Mantenimiento de Clientes",width="fill", height="fill",command=mantenimiento_clientes )
 button = PushButton(app,text="Registrar Usuario",width="fill", height="fill",command= mantenimiento_clientes)
 button = PushButton(app,text="Registrar Vehiculo",width="fill", height="fill",command= admin_vehiculos)
 button = PushButton(app,text="Realizar Cita",width="fill", height="fill",command= realizar_cita )
 button = PushButton(app,text="Administrar Empleados",width="fill", height="fill",command= registrar_empleado)
 button = PushButton(app,text="Estado del Vehiculo",width="fill", height="fill",command= admin_vehiculos)
 
 
 app.display()     
 
#menu_taller () 
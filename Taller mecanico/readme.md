***********    LLUVIA DE IDEAS PARA LA BASE DE DATOS  ***********************

- Se comenzo haciendo el diagrama entidad relacion del enunciado del proyecto.
haciendo las tablas para cita, cliente, vehiculo y para los mecanicos y asesores.

- Leyendo con detenimiento el enunciado se solicita que el mecanico y el asesor contengan la misma informacion y sean diferenciaciados por el atributo Tipo en el cual se especificara si el "empleado" es un mecanico o un asesor. Para eso despues de revisar la documentacion de la clase se llego a la conclusion de que esa entidad era reflexia (se llamaba asi misma) puesto que un asesor es el encargado de los mecanicos. Tomando como referencia un ejemplo dado en la clase sobre un gerente dirigiendo a sus empleados. La tabla empelado llevara una FK que hace referencia a la misma tabla, añadiendole un atributo id_empelado_asesor para hacer la referencia del cargo asesor.

- RELACIONES CON LAS TABLAS
Tomando como guia algunas referencias de ejemplos de videos encontrados en youtube realizamos la cardinalidad de las tablas de la siguiente manera:

CITA-CLIENTE

1. Cual es la cantidad minima de citas que pide a un cliente 1
2. Cual es la cantidad maxima de citas que pide a un cliente n
3. Cual es la cantidad minima de clientes que tiene una cita 1
4. Cual es la cantidad maxima de clientes que tiene una cita 1
cardinalidad es de (n:1)

CLIENTE-VEHICULO
1. Cual es la cantidad minima de clientes que tiene un vehiculo 1
2. Cual es la cantidad maxima de clientes que tiene un vehiculo 1
3. Cual es la cantidad minima de Autos que tiene un cliente 1
4. Cual es la cantidad maxima de autos que tiene un cliente n
cardinalidad es de (1:n)

VEHICULO-MECANICO
1. Cual es la cantidad minima de vehiculos que repara un mecanico. 0
2. Cal es la cantidad maxima de vehiulos que repara un mecanico. n
3. Cual es la cantidad minima de mecanicos que reparan un vehiculo. 1
4. Cual es la cantidad maxima de mecanicos que reparan un vehiculo. n
la cardinalidad es de (n:n)

VEHICULO-MECANICO
1. Cual es la cantidad minima de vehiculos que da mantenimiento un mecanico 0
2. Cual es la cantidad maxima de vehiculos que da mantenimiento un mecanico n
3. Cual es la cantidad minima de mecanicos que da mantenimiento a un vehiculo 1
4. Cual es la cantidad maxima de mecanicos que da mantenimiento a un vehiculo n
cardinalidad es de (n:n)

CITA-EMPLEADO
1. Cual es la cantidad minima de citas que puede tener un mecanico 0
2. Cual es la cantidad maxima de citas que puede tener un mecanico n
3. Cual es la cantidad minima de mecanicos que puede tener una cita 1
4. Cual es la cantidad maxima de mecanicos que puede tener una cita n
la Cardinalidad es de (n:n)

ASESOR-MECANICO
1. Cual es la cantidad minima de mecanicos que dirige un asesor 1
2. Cual es la cantidad maxima de mecanicos que dirige un asesor n 
3. Cual es la cantidad minima de asesores que tiene un mecanico 1
4. Cual es la cantidad maxima de asesores que tiene un mecanico 1
la cardinalidad es de (n:1)

-REALIZANDO EL MAPEO DE LAS TABLAS
teniendo una vez el diagrama entidad relacion con sus respectivas relaciones se procedio a crear el mapeo guiandonos del modelo entidad relacion.

-CREACION DE LA BASE DE DATOS EN POSTGRESQL 

Se procedio a instalar el la intergazgrafica del software postgresql que nos facilitara la creacion del SQL para la base de datos ayudandonos de:
PRIMARY KEY : para el id de cada tabla 
VARCHAR : para nombre, descripciones, correo electronico etc.
BIGINT : Para las id ya que se iran incremntando en mayor cantidad con el paso del tiempo.
DATE: para la fecha de entreha y fecha de entrada.
TIME: para la hora de entrada y los limites de cupos en las citas
UNIQUE: para dejar unicos los correos electronicos 

- CREAR EL CODIGO PARA LA INTERFAZ USANDO PYTHON CON LA LIBRERIA TKINTER. 

Se decidio utilizar el lenguaje PYTHON ya que contiene una libreria llamada tkinter que permite diseñar interfaces graficas de una manera mas sencilla.

Para la conexion entre postgresql y python utilizaremos los cripts conocidos para la conexion y adicional a eso se implementara herencia con lo cual en cada pestaña que se cree para hacer el programa estara relacionada con la conexion a la base dedatos por lo que no sera neceseracia crearla en cada archivo.bbb

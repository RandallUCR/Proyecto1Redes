# Proyecto1Redes

Los programas necesarios para la creacion de este proyecto:

1.Python 
2.Pycharm(opcional)
3.MySQL server
4.MySQL Workbench

Descripcion

1. Python es un lenguaje de programación interpretado cuya filosofía hace énfasis en la legibilidad de su código Hablamos de un lenguaje de programación multiparadigma, debido a que soporta orientación a objetos, programación imperativa y, en menor medida, programación servible. Es cualquier lenguaje interpretado, dinámico y multiplataforma.

Para instalar Python 3.7 en cualquier equipo con el sistema operativo Windows 7, 8, 8.1 o 10 usar una cuenta de cliente con privilegios de administrador, o bien, nuestra cuenta del administrador local. Por estabilidad, se puede agregar -temporalmente- para este proceso de instalación la contabilización del cliente presente al conjunto local Administradores. Para eso, comenzar la aplicación de Gestión de conjuntos, entrar a la herramienta del sistema Usuarios y equipos locales y agregar la contabilización presente a comentado conjunto.

En los sistemas con arquitectura 64 bit se puede instalar tanto la versión de Python para 32 bit como para 64 bit. Generalmente, laborar con la versión para 64 bit optimización el rendimiento y posibilita que cualquier programa logre usar bastante más de 4 Gb de RAM, memoria límite en sistemas 32 bit. Comúnmente, haciendo un trabajo por abajo de este límite no se observan diferencias de rendimiento relevantes entre las dos versiones sin embargo se recomienda instalar la versión de 64 bit. Sí o sí, si se van a usar módulos de terceros, conviene verificar si permanecen disponibles para la versión a instalar.

Tambien se deben instalar las librerias mysql-conector-python y tkcalendar para eso seleccionamos el proyecto, nos vamos a file, settings, le damos al boton de + y buscamos la libreria que deseamos la seleccionamos y la instalamos.


2. PyCharm es un entorno  de desarrollo integrado (IDE) usado en la programación de computadoras , especialmente para el lenguaje Python . Está desarrollado por la compañía checa JetBrains . Otorga estudio de código, cualquier depurador gráfico, cualquier probador de unidades integrado, integración con sistemas de control de versiones (VCSes) y admite el desarrollo web con Django , como la ciencia de datos con Anaconda .

Para instalarlo basta con ir a la pagina oficial y descargar el ejecutable.

3. MySQL es un sistema de administración de bases de datos relacional desarrollado bajo licencia dual: Licencia pública general/Licencia comercial por Oracle Corporation y está considerada como la base de datos de código abierto más habitual de todo el mundo,y una de las más populares generalmente junto a Oracle y Microsoft SQL Server, todo para espacios de desarrollo web.
MySQL ha sido al inicio desarrollado por MySQL AB (empresa establecida por David Axmark, Allan Larsson y Michael Widenius). MySQL AB ha sido adquirida por Sun Microsystems en 2008, y ésta paralelamente ha sido comprada por Oracle Corporation en 2010, la cual ya era dueña a partir de 2005 de Innobase Oy, compañía finlandesa inventora del motor InnoDB para MySQL.

Para instalar MySQL Server y MySQL Workbench es necesario ir a esta direccion https://dev.mysql.com/downloads/mysql/ e instalar el MySQL Installer este ejecutable te da la opcion de instalar muchas cosas como coneccion con varios lenguajes de programacion entre estos python y tambien para instalar los dos ultimos programas que son escenciales.

Manual de tecnico.

En el proyecto existen varios archivos:

  1.Server.py
  2.Client.py
  3.Configuration.py
  4.ServerUI.py

1. Server.py es el archivo donde se encuentra el codigo para iniciar el servidor y comience a escuchar para que los clientes pueden conectarse. Se levanta una interfaz que esta albergada en el archivo ServerUI.py. Este archivo tiene los siguentes metodos.
  * worker(*args)

Este metodo se encarga de enviar y recibir datos de los cliente, de crear un nuevo hilo para cada cliente nuevo y este espacio un programador puede manipular el protocolo de envio y obtencion de datos de cliente y servidor.

2. Client.py en este archivo es donde esta la mayoria de la logica del proyecto pues en el mismo se en ecuentra los metodos mas importantes como md5() que se encarga de obtener la firma de cada uno de los archivos que sean seleccionado en el mismo no hay mucho que se puede modificar, tambien se encuentra el metodo programar() que se encargar de las programaciones de las tareas en un dia,fecha y hora exacta para la ejecucion del escaneo, en esta parte se pueden modificar el formato de hora, el metodo interfaz() como su nombre lo indica levanta la ventana en este se puede modificar lo visual para hacerlo mas atractivo y en el metodo main() se envia y recibe informacion del servidor , se puede modificar el protocolo de comunicacion con le servidor y tambien la deteccion de virus o hashes maliciosos haciendo el uso del metodo comparar() utiliza dos listas una contiene las firmas locales y la otra las firmas recibidas del servidor.

3. Configuration.py es el archivo que esta encargado de la conexion de python con le base de datos en MySQL y solo cuenta con el metodo listar_hashs(), en este metodo lo que se hace es la conexion con la base de datos se puede modificar los datos de conecion como nombre o contraseña y ademas de esto obtniene las firmas almacenadas en la base de datos para poder enviarselas al cliente no recomiendo cambiar absolutamente nada excepto la parte de conexion con la base de datos.

4. Server.UI este es la interfaz del servidor, en este archivo solo se encuentra codigo meramente estetico se utiliza para monstrar una ventana que muestre los clientes activos, los hashes maliciosos encontrados por los clientes, y los hashes almacenados en la base de datos. Los cambios que se pueden realizar en esta parte solo afectaran de forma visual el proyecto.




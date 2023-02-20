from ast import Expression
import os

CARPETA= 'contactos/' #carpeta de contactos
EXTENSION= '.txt'   #extension de archivos

class Contacto:
    def __init__(self,nombre, telefono, categoria):
        self.nombre=nombre
        self.telefono= telefono
        self.categoria= categoria
        

def app():
    #Revisa si la carpeta existe o no
    crear_directorio()

    #muestra el menú de opciones
    mostrar_menu()
    
    #preguntar al usuario la accion a realizar
    preguntar=True

    while preguntar:
        opcion=input('Seleccione una opción: \r\n')
        opcion=int(opcion)

        #Ejecutar las opciones
        if opcion== 1:
            print('Agregar Contacto')
            agregar_contacto()
            preguntar=False
        elif opcion== 2:
            print('Editar Contacto')
            editar_contacto()
            preguntar=False
        elif opcion== 3:
            mostrar_contactos()
            preguntar=False
        elif opcion== 4:
            print('Buscar Contacto')
            buscar_contactos()
            preguntar=False
        elif opcion== 5:
            print('Eliminar Contacto')
            eliminar_contacto()
            preguntar=False
        else:
            print('Opcion No valida, intente de nuevo')   

def eliminar_contacto():
    nombre = input('Selecione el contacto que desea eliminar \r\r')
    try:
        os.remove(CARPETA+nombre+EXTENSION)
        print('\r\nEliminado correctamente')
    except expression as identifier:
        print('No existe el contacto')

    app()
def buscar_contactos():
    nombre = input('Selecione el contacto que desea buscar \r\r')
    try:
        with open (CARPETA+ nombre +EXTENSION) as contacto:
            print('\r\n Informacion del contacto \r\n')
            for linea in contacto:
                print(linea.rstrip())
            print('\r\n')
    except IOError:
        print('El archivo no existe')

    app()

def mostrar_contactos():
    archivos = os.listdir(CARPETA)
    archivo_txt = [i for i in archivos if i.endswith(EXTENSION)]

    for archivo in archivo_txt:
        with open (CARPETA + archivos) as contacto:
            for linea in contacto:
                print(linea.rstrip())
            print('\r\n')
    app()
def editar_contacto():
    print('Escribe el nombre del contacto a editar')
    nombre_anterior=input ('Nombre del contacto que deseas editar: \r\n')
    #Revisar si el archivo ya existe antes de editarlo
    existe= exite_contacto(nombre_anterior)

    if existe:
        with open(CARPETA + nombre_anterior+EXTENSION, 'w') as archivo:
            #Resto de los campos
            nombre_contacto = input ('Agrega el nuevo nombre: \r\n')
            telefono_contacto = input ('Agrega el nuevo telefono: \r\n')
            categoria_contacto = input ('Agrega la nuevaCategoria contacto: \r\n')
            
            #instanciar
            contacto=Contacto(nombre_contacto,telefono_contacto,categoria_contacto)
            
            #Escribir en el archivo
            archivo.write('Nombre: '+ nombre_contacto+ '\r\n')
            archivo.write('Telefono: '+ telefono_contacto+ '\r\n')
            archivo.write('Categoria: '+ categoria_contacto+ '\r\n')

            #renombrar el archivo
            os.rename(CARPETA + nombre_contacto +EXTENSION,CARPETA +  nombre_contacto +EXTENSION)
            print('\r\n Contacto editado correctamente')
    else:
        print('Ese contacto no existe')

#REiniciar
    
    app()
def agregar_contacto():  
    print('Escribe los datos para agregar el nuevo contacto')
    nombre_contacto = input ('Nombre del Contacto \r\n')

    #revisar si el archivo ya existe antes de crearlo
    existe=os.path.isfile(CARPETA + nombre_contacto+EXTENSION)
    if not existe:

        with open(CARPETA + nombre_contacto+EXTENSION, 'w') as archivo:

        #instanciar clases
            telefono_contacto=input('Agregar el telefono: \r\n')
            categoria_contacto=input('Categoria contacto: \r\n')

            #iniciar la clase
            contacto=Contacto(nombre_contacto,telefono_contacto,categoria_contacto)
            archivo.write('Nombre: '+ nombre_contacto+ '\r\n')
            archivo.write('Telefono: '+ telefono_contacto+ '\r\n')
            archivo.write('Categoria: '+ categoria_contacto+ '\r\n')

            #mostrar un mensaje de exito
            print('\r\n Contacto creado correctamente \r\n')
    else:
        print('Este usuario ya existe')

    #reiniciar app
    app()
def mostrar_menu():
    print('Seleccionar del Menu lo que desea hacer:\r\n')
    print('1) Agregar nuevo Contacto')
    print('2) Editar Contacto')
    print('3) Ver Contactos')
    print('4) Buscar Contacto')
    print('5) Eliminar')

def crear_directorio():
    if not os.path.exists(CARPETA):
        #Crear la carpeta
        os.makedirs(CARPETA)

def exite_contacto(nombre):
    return os.path.isfile( CARPETA+ nombre +EXTENSION) 

app()
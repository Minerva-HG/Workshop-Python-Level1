#Creando un diccionario simple
cancion ={
    'artista':'Metallica',
    'cancion': 'Enter Sadman',
    'Lanzamiento': 1992,
    'likes': 3000
}

#acceder a los elementos del diccionario
print (cancion['artista'])
print (cancion['Lanzamiento'])

#mezclar con un string
artista= cancion['artista']
print (f'Estoy escuchando a {artista}')

print (cancion)

#agregar nuevos valores
cancion['playlist'] = 'Heavy Metal'
print (cancion)

#Reemplazar valores existentes
cancion['cancion']='Seek & Destroy'
print(cancion)

#eliminar un valor
del cancion['Lanzamiento']
print (cancion)


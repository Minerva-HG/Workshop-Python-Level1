playlist = {} #Diccionario vacio
playlist['canciones'] =[] #Lista vacia de canciones

#funcion principal
def app():
    #agregar la playlist
    agregar_playlist=True
    while agregar_playlist:
            nombre_playlist= input('Como deseas nombras la playlist?\r\n')
            if nombre_playlist:
                playlist['nombre']= nombre_playlist
        #ya tenemos un nombre, desactivar el true
            agregar_playlist= False
            agregar_canciones()
            #print(playlist)
def agregar_canciones():
    agregar_cancion=True
    while agregar_cancion:
        nombre_playlist=playlist['nombre']
        pregunta= f'\r\n Agrega canciones para la playlist {nombre_playlist}: \r\n'
        pregunta+='Escribe "X" para dejar de agregar canciones \r\n'
        
        cancion=input(pregunta)
        if cancion=='X':
            #dejar de agregar canciones
            agregar_cancion= False

            mostrar_resumen()
            #print('Finalizado')
        else:
            #Agregar las canciones a la playlist
            playlist['canciones'].append(cancion)

            print(playlist)
 
def mostrar_resumen():
    nombre_playlist= playlist['nombre']
    print(f'Playlist:{nombre_playlist}\r\n')
    print('Canciones:\r\n')
    for cancion in playlist['canciones']:
        print(cancion)


app()


#iniciar con un diccionario vacio
jugador={}
print(jugador)

#se une un jugador
jugador['nombre']='Juan'
jugador ['Puntaje']=0
print(jugador)

#incremento el puntaje
jugador['puntaje']=100
print (jugador)

#incremento el puntaje
jugador['puntaje']=200
print (jugador)

#acceder a un valor
print(jugador.get('Consola', 'No existe este valor'))

#iterar en el diccionarop
for llave, valor in jugador.items():
    print(llave)
    print(valor)


#eliminar jugador y puntaje
#del jugador ['nombre'] ='Juan'
#del jugador ['puntaje'] = 0
#print(juagador)

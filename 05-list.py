lenguajes = ['Python','Kotlin','Java','JavaScript']

print(lenguajes)
#Los arrays (list) comienza en la posición 0
print(lenguajes[0]) #python

#ordenar los elementos
lenguajes.sort()
print(lenguajes)

#acceder a un elemento dentro de un texto
aprendiendo= f'Estoy aprendiendo {lenguajes[3]}'
print(aprendiendo)

#Modificando valores de un arreglo
lenguajes[2]= 'PHP'
print (lenguajes)

#Agregar elementos a un arreglo
lenguajes.append('Ruby')
print(lenguajes)

#eliminiar un elemento del arreglo
del lenguajes[1]
print(lenguajes)

#Eliminar de otra manera
lenguajes.pop() #elimina el ultimo elemento
print(lenguajes)

lenguajes.pop(0) #elimina una posicion especifico
print(lenguajes)

'''
lenguajes.remove('PHP') #elimina una posicion especifico
print(lenguajes)'''
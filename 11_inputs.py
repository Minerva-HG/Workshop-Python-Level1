#inputs
#nombre=input('Cúal es tu nombre: \r\n')
#print(f'Hola {nombre}')

#leer datos que serán numeros

edad = input ('Cúal es tu edad? \r\n')

#Convertir edad (string) a int
edad= int(edad)
if edad >=18:
    print('Ya puedes votar')
else:
    print('Aun no puedes votar')

#mezclar operadores
numero = input('Agrega un numero y te dire si es par o non \r\n')

numero=int(numero)

if numero % 2 ==0:
    print(f'El numero {numero} es par')
else:
    print(f'el numero {numero} es impar')





    
#mezclar operadores
pregunta='Agregar un numero y te dire si es para o imprar \r\n'
pregunta +='(Escribe "Cerrar" para salir de la aplicacion)\r\n'

preguntar=True
while preguntar:

    numero = input(pregunta)

    if numero =='Cerrar':
        preguntar=False
    else:
        numero= int(numero)

        if numero % 2 ==0:
            print(f'el numero {numero} es par')
        else:
            print(f'El numero {numero} es impar')

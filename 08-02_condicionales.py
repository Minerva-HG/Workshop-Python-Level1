#Ejemplo de condicionales con elif

ocupacion = 'Estudiante'

if ocupacion=='Estudiante':
    print('Tienes 50% de descuento')
elif ocupacion=='Jubilado':
    print('Tienes el 75% de descuento')
elif ocupacion=='Desempleado':
    print('tienes un 10% de decuento')
else:
    print('Debes de pagar el 100%')
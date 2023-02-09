#operadores and y or

usuario1= True
usuario2= False

if usuario1 and usuario2:
    print('Administrador')
else:
    print('Debes iniciar sesión')

usuario1= True
usuario2= False

if usuario1 or usuario2:
    print('Administrador')
elif usuario2:
    print('Acceso al sistema')
else:
    print('Debes iniciar sesión')

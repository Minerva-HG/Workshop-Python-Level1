#condicionales

balance= 500
if balance > 0:
    print('puedes pagar')
else:
    print('no tiene saldo')

#likes
likes=200
if likes >200:
    print('excelente, 200 likes')
else:
    print('casi llega a los 200 likes')


#if contexto
lenguaje= 'Python'

if lenguaje == 'Python':
    print('excelente desicion')

lenguaje2= 'python'

if  lenguaje2 == 'PHP':
    print('excelente desicion')
else:
    print('que chafa ')


lenguaje2= 'python'

if not lenguaje2 == 'PHP':
    print('excelente desicion')
else:
    print('que chafa ')


#boolean

usuario_autenticado= True
if usuario_autenticado==True:
    print('Acceso al sistema')
else:
    print('debes iniciar sesión')
    
# evaluar un elemento en la lista
lenguajes = ['Python','Kotlin','Java','JavaScript']

if 'PHP' in lenguajes:
    print('PHP si existe')
else:
    print('No no esta en la lista')


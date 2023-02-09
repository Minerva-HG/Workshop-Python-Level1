

#pregunta1='Si'
valor=0

pregunta1= input('tu perro se llama Molly? \r\n')
pregunta1= input('tu perico se llama paco? \r\n')
pregunta1= input('tu gato se llama snacho? \r\n')
pregunta1=int(pregunta1)

for val in valor:
    if pregunta1=='si':
        val=val+1
    else:
        val=val-1

#val=int(val)
print (val)
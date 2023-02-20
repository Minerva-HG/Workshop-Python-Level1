def app():
    archivo= open('archivo','w')

    for i in range (0,20):
        archivo.write('Esta es una linea'+str(i)+"\r\n")
    
    archivo.close()
    
app()
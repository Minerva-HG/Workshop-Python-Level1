def app():
    with open('C:\Proyectos\Python\archivo') as archivo:
        for contenido in archivo:
            print(contenido.rstrip())

app()
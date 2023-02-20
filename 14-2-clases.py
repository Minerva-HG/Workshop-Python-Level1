class Restaurant:
    def __init__(self, nombre, categoria, precio):
        self.nombre=nombre
        self.categoria=categoria
        self.precio=precio

    def mostrar_informacion(self):
        print(f'Nombre: {self.nombre}, Categoria:{self.categoria}, Precio:{self.precio}')

#instanciar la clase

restaurant=Restaurant('Pizzeria Mexico','Comida Italiana',50)
restaurant.mostrar_informacion()

restaurant2=Restaurant('Hamburguesas python','Comida Casual',20)
restaurant2.mostrar_informacion()

#mostrar la informacion
#print(f'Nombre Restaurant: {restaurant.nombre}')
#print(f'Nombre Restaurant: {restaurant2.nombre}')
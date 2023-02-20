class Restaurant:
    def agregar_restaurant(self, nombre):
        self.nombre=nombre  #atrubuto

    def mostrar_informacion(self):
        print(f'Nombre: {self.nombre}')

#instanciar la clase
restaurant=Restaurant()
restaurant.agregar_restaurant('Pizzeria Mexico')
restaurant.mostrar_informacion()

restaurant2=Restaurant()
restaurant2.agregar_restaurant('Hamburguesas python')
restaurant2.mostrar_informacion()

#mostrar la informacion
print(f'Nombre Restaurant: {restaurant.nombre}')
print(f'Nombre Restaurant: {restaurant2.nombre}')
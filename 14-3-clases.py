class Restaurant:
    def __init__(self, nombre, categoria, precio):
        self.nombre=nombre
        self.categoria=categoria
        self.precio=precio # defaul:public // se puede modificar en cualquier parte
        #self._precio=precio # Protected// modificado en la misma clase
        self.__precio=precio #private// solo por medio de un metodo se puede acceder
        

    def mostrar_informacion(self):
        print(f'Nombre: {self.nombre}, Categoria:{self.categoria}, Precio:{self.__precio}')

#instanciar la clase
#getters and setter -get = obtiene un valor, set = agrega un valor
def get_precio(self):
    return self.__precio

def set_precio(self,precio):
    self.__precio = precio

restaurant=Restaurant('Pizzeria Mexico','Comida Italiana',50)
#print(restaurant._precio)  #NO ES POSIBLE MODIFICARLO si fuera de esta forma print(restaurant._precio) 
#restaurant.precio=80
restaurant.mostrar_informacion()
restaurant.set__precio(80)
precio=restaurant.get__precio()
print(precio)

restaurant2=Restaurant('Hamburguesas python','Comida Casual',20)
#print(restaurant._precio)
#restaurant.precio=40
restaurant2.mostrar_informacion()
restaurant2.set__precio(40)
restaurant2.get__precio()

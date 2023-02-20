#Herencia
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

#Crear una clase hijo de restaurante
class Hotel (Restaurant):
    def __init__(self, nombre, categoria, precio):
        super().__init__(nombre, categoria, precio)

hotel= Hotel('Hotel POO', '5 Estrellas', 200)
hotel.mostrar_informacion()
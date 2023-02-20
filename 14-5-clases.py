#polimorfismo
class Restaurant:
    def __init__(self, nombre, categoria, precio):
        self.nombre=nombre
        self.categoria=categoria
        self.precio=precio # defaul:public // se puede modificar en cualquier parte
        #self._precio=precio # Protected// modificado en la misma clase
        #self.__precio=precio #private// solo por medio de un metodo se puede acceder
        

    def mostrar_informacion(self):
        print(f'Nombre: {self.nombre}, Categoria:{self.categoria}, Precio:{self.precio}')

#instanciar la clase
#getters and setter -get = obtiene un valor, set = agrega un valor
    def get_precio(self):
        return self.precio

    def set_precio(self,precio):
        self.precio = precio

#Crear una clase hijo de restaurante
class Hotel (Restaurant):
    def __init__(self, nombre, categoria, precio,alberca):
        super().__init__(nombre, categoria, precio)
        self.alberca=alberca

    def mostrar_informacion(self):
        print(f'Nombre: {self.nombre}, Categoria:{self.categoria}, Precio:{self.precio}, Alberca: {self.alberca}')

    #Agregar un metodo que solo exista en Hotel
    def get_alberca(self):
        return self.alberca

hotel= Hotel('Hotel POO', '5 Estrellas', 200,'Si')
hotel.mostrar_informacion()
alberca=hotel.get_alberca()
print(alberca)
class Restaurante:
    def __init__ (self,nombre,categoria,precio):
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio
    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}, Categoria: {self.categoria}, Precio: {self.precio}")
#Instanciar la clase
restaurante = Restaurante("Pizzeria Mexico", "KFC", 55)
restaurante.mostrar_informacion()

restaurante2 = Restaurante("Pizzeria Mexico", "KFC", 20)
restaurante2.mostrar_informacion()
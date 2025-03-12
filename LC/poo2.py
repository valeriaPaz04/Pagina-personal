class Restaurant:

    def __init__ (self,nombre,categoria):
        self.nombre = nombre
        self.categoria = categoria
    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}, Categoria: {self.categoria}")
#Instanciar la clase
restaurant = Restaurant("Pizzeria Mexico", "KFC")
restaurant.mostrar_informacion()

restaurant2 = Restaurant("Pizzeria Mexico", "KFC")
restaurant2.mostrar_informacion()
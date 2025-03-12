#Ejercicio 1
jugador = {}

#primer jugador
jugador ["nombre"] = "Luis"
jugador ["puntaje"] = 0
print(jugador)

jugador ["puntaje"] = 80
print(jugador)

for llave, valor in jugador.items():
    print (llave)
    print (valor)

#segundo jugador
jugador ["nombre"] = "Edwin"
jugador ["puntaje"] = 0
print(jugador)

jugador ["puntaje"] = 120
print(jugador)

for llave, valor in jugador.items():
    print (llave)
    print (valor)



#Ejercicio 2
nombre = input("Cual es tu nombre? ")
print(f"Saludos {nombre}")

edad = input("Digame su edad ")
edad = int(edad)

if edad >= 18:
    print("Puedes votar")
else:
    print("No puedes votar")



#Ejercicio 3
pregunta = "Puede agregar un número y diré si es par o impar"
pregunta += " o escriba cerrar para salir de la aplicación "

preguntar = True

while preguntar:

    numero = input(pregunta)

    if numero == "cerrar":
        pregunta = False
    else:
        numero = int(numero)

        if numero % 2 == 0:
            print(f"El numero {numero} es par")
        else:
            print(f"El numero {numero} es impar")



#Ejercicio 4
numero = 0

while numero <= 10:
    print(numero)
    numero += 1 #se incrementa de a 1 para evitar el ciclo infinito

#if dentro del while
while numero <= 10:
    if numero == 5:
        break
    else:
        print(numero)
    numero += 1
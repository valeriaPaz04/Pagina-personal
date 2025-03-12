# Ejercicio 1
nombre_usuario = input("Escriba su nombre ")
nombre_mayuscula = nombre_usuario.upper()
cantidad_numeros = len(nombre_usuario)
print(f"Tu nombre {nombre_mayuscula}, tiene {cantidad_numeros} letras")

# Ejercicio 2
precio_barra = 3.49
descuento = 0.60

barras_vendidas = int(
    input("Digite el numero de barras vendidas que no son del dia "))

descuento_barra = precio_barra * descuento
precio_con_descuento = precio_barra - descuento_barra
precio_final = barras_vendidas * precio_con_descuento

print(f"Precio habitual de una brra de pan: {precio_barra} euros")
print(f"Descuento por no ser fresca: {precio_con_descuento} euros")
print(f"Coste total a pagar: {precio_final} euros")

# Ejercicio 3
creditos = {"Matematicas": 6, "Fisica": 4, "Quimica": 5}
Matematicas = creditos["Matematicas"]
Fisica = creditos["Fisica"]
Quimica = creditos["Quimica"]

print(f"Matemáticas tiene {Matematicas} créditos")
print(f"Matemáticas tiene {Fisica} créditos")
print(f"Matemáticas tiene {Quimica} créditos")

# Ejercicio 4
asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]

# Lista para almacenar las notas
notas = []

# Pedir la nota de cada asignatura
notas.append(float(input("Introduce la nota de Matemáticas: ")))
notas.append(float(input("Introduce la nota de Física: ")))
notas.append(float(input("Introduce la nota de Química: ")))
notas.append(float(input("Introduce la nota de Historia: ")))
notas.append(float(input("Introduce la nota de Lengua: ")))

# Lista para almacenar las asignaturas a repetir
asignaturas_repetir = []

# Revisar qué asignaturas se deben repetir
if notas[0] < 3.0:
    asignaturas_repetir.append("Matemáticas")
if notas[1] < 3.0:
    asignaturas_repetir.append("Física")
if notas[2] < 3.0:
    asignaturas_repetir.append("Química")
if notas[3] < 3.0:
    asignaturas_repetir.append("Historia")
if notas[4] < 3.0:
    asignaturas_repetir.append("Lengua")

# Mostrar asignaturas a repetir
if len(asignaturas_repetir) > 0:
    print("Debes repetir las siguientes asignaturas:")
    print(asignaturas_repetir)
else:
    print("Has aprobado todas las asignaturas.")

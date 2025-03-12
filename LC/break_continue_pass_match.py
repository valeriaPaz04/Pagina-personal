#break
nombre = ""

while True:
    nombre = input("Ingrese su nombre ")
    if nombre !="":
        break

#continue
telefono = "1235-768-087"

for i in telefono:
    if i in telefono:
        if i =="-":
            continue
    print(i, end="")

#pass
for i in range (1,21):
    if i == 13:
        pass
    else:
        print(i)

#match
print("menú de opciones")
print("[1] Ventas")
print("[2] Soporte")
print("[3] Administración")
print("[4] RecursosH")
opcion = int(input("Elegir opción "))

match opcion:
    case 1:
        print("VENTAS")
    case 2:
        print("SOPORTE")
    case 3:
        print("ADMINISTRACIÓN")
    case 4:
        print("RecursosH")
    case _:
        print("Opcion inexistente")

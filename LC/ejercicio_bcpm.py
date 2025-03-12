num_uno = int(input("Ingrese un número "))
num_dos = int(input("Ingrese otro número "))

print("Elija la operación para hacer")
print("[1] Suma (+)")
print("[2] Resta (-)")
print("[3] Multiplicación (x)")
print("[4] División (/)")
opcion = int(input("Elija una opción "))

match opcion:
    case 1:
        suma = num_uno + num_dos
        print(f"El resultado de la suma es {suma}")
    case 2:
        resta = num_uno - num_dos
        print(f"El resultado de la resta es {resta}")
    case 3:
        multiplicacion = num_uno * num_dos
        print(f"El resultado de la multiplicacion es {multiplicacion}")
    case 4:
        division = num_uno / num_dos
        print(f"El resultado de la division es {division}")
    case _:
        print("Opcion inexistente")
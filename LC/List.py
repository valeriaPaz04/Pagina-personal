nombres_amigos = ["Edwin", "Emiliano", "Daniel", "Sara"]

print(nombres_amigos)

#Los arrays (lists)
print(nombres_amigos[3])
print(nombres_amigos[0])
print(nombres_amigos[2])
print(nombres_amigos[1])

bebidas = ["hit", "cafe", "monster"]

bebidas.sort() #pone los elementos en orden alfabetico
print(bebidas)

tomar = f"Estoy tomando {bebidas[0]}"
print(tomar)

bebidas.append("gaseosa") #agregar un elemento
print(bebidas)

del bebidas[1] #eliminar un elemento
print(bebidas)

bebidas.pop() #eliminar el ultimo elemento
print(bebidas)

bebidas.pop()
print(bebidas[3]) #eliminar el elemento indicado
anos=0
dias=0
meses=0
semana=0

Num_dias=int(input("ingrese el numero de dias a ser convertido:"))

dias = Num_dias
while dias > 365:
    anos = anos + 1
    dias = dias - 365 

while dias > 30 : 
    meses = meses + 1
    dias = dias - 30

while dias > 7 :
    semana = semana + 1
    dias = dias - 7

print(f'En {Num_dias} hay dias \nHay {anos} años\n{meses} Meses\ncon {semana} semanas y\n{dias} dias  ')
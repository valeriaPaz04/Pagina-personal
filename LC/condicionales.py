#Tarjeta continuar si tiene saldo o no
tarjeta = 500
if tarjeta > 0:
    print("Puedes pagar")
else:
    print("No puedes pagar")


#Muestra cantidad de likes
likes = 200
if likes == 200:
    print("Tienes 200 likes, influencer")
else:
    print("No tienes likes")


#Saber si un elemento esta en la lista
dias = ["lunes", "martes", "miercoles", "jueves"]

if "viernes" in dias:
    print("El dia viernes si esta en la lista")
else:
    print("El dia viernes no esta en la lista")


#Acceso a usuario
usuario_autenticado = True
usuario_Dba = True
if usuario_autenticado:
    if usuario_Dba:
        print("Acceso aceptado")
    else:
        print("Acceso normal")
else:
    print("Debe registrarse en el sistema")


#Rol
rol = "estudiante"
if rol == "instructor":
    print("Tienes el 40% de descuento")
elif rol == "estudiante":
    print("Tienes el 60% de descuento")
else:
    print("No tienes descuento, debes pagar el 100%")


#Administrador
usuario_loogeado = True
usuario_admin = False
if usuario_loogeado and usuario_admin:
    print("Administrador")
elif usuario_loogeado:
    print("Acceso al sistema")
else:
    print("Debes iniciar seccion")

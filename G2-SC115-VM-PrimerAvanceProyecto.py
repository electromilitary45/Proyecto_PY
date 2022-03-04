#---variables---
user="admin"
passw="admin"

#----/LOGIN---/

usuario=""
passw=""
while usuario !="admin" or passw !="admin":
    usuario=input("Introduzca su usuario: ")
    passw=input("Introduzca su contraseña: ")
    if usuario=="admin" and passw =="admin":
        tipoReg=int(input("Que quiere registrar? (1.Visitantes 2.Agenda de visita):"))
        if tipoReg==1:
            print("----------------\nComplete lo solicitado!")
            nomCom=input("Nombre completo: ")
            id=int(input("Cédula: "))
            phoneNum=int(input("Número de teléfono: "))
            email=input("Correo electrónico: ")
            address=input("Direccion: ")
            nacionalidad=int(input("Digite si usted es '1.Nacional' o '2.Extrangero': "))
            ageG=int(input("Digite si es 1.Niño, 2.Adulto o 3.Adulto mayor: "))
            print("Registro Exitoso para el usuario",nomCom)
        else:
            print("¡Esta opción no está disponible!")
    else:
        print("Su usuario no fue encontrado")


# userIn=input("Introduzca su usuario: ")
# passwIn=input("Introduzca su contraseña: ")
# if userIn== user and passwIn== passw:
#     tipoReg=int(input("Que quiere registrar? 1.Visitantes 2.Agenda de visita"))
#     if tipoReg==1:
#         print("----------------\nCompleto lo solicitado!")
#         nomCom=input("Nombre completo: ")
#         id=int(input("Cédula: "))
#         phoneNum=int(input("Número de teléfono: "))
#         email=input("Correo electrónico: ")
#         address=input("Direccion: ")
#         nacionalidad=int(input("Digite si usted es '1.Nacional' o '2.Extrangero': "))
#         ageG=int(input("Digite si es 1.Niño, 2.Adulto o 3.Adulto mayor: "))
        
#         print("Registro Exitoso para el usuario",nomCom)
#     else:
#         print("¡Esta opción no está disponible!")
# else:
#     print("Usuario no encontrado")





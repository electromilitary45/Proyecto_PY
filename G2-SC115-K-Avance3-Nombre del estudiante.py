#---------------librerias-------------
import os
from tkinter import N

#---------------Funciones--------------------------------
def visitantes():
    file=open("visitantes.txt","a") #"a" escribir sin borrar
    file.close()
    
    print("----------------\nComplete lo solicitado para registar al visitante 👤:")
    nomCom=input("Nombre completo👤 : ")
    id=int(input("Cédula 🆔: "))
    phoneNum=int(input("Número de teléfono ☎️: "))
    email=input("Correo electrónico 📧:  ")
    address=input("Dirección: 🧭 ")
    nacionalidad=int(input("Digite si usted es '1.Nacional' o '2.Extrangero' 👤: "))
    ageG=int(input("Digite si es 1.Niño, 2.Adulto o 3.Adulto mayor 🧍🏾: "))
    print("Registro exitoso para el usuario",nomCom,"✅")
    if nacionalidad==1:
        nacionalidad="Nacional"
        file=open("visitantesNac.txt","a") #"a" escribir sin borrar
        file.write("Nombre: "+nomCom+"\n"+"Cédula: "+str(id)+"\n"+"Teléfono: "+str(phoneNum)+"\n"+"Correo Electrónico: "+email+"\n"+"Dirección: "+address+"\n"+"Nacionalidad: "+nacionalidad+"\n"+"Edad: "+str(ageG)+"\n"+"------------\n")
        file.close()
    else:
        nacionalidad="Extrangero"
        file=open("visitantesExt.txt","a") #"a" escribir sin borrar
        file.write("Nombre: "+nomCom+"\n"+"Cédula: "+str(id)+"\n"+"Teléfono: "+str(phoneNum)+"\n"+"Correo Electrónico: "+email+"\n"+"Dirección: "+address+"\n"+"Nacionalidad: "+nacionalidad+"\n"+"Edad: "+str(ageG)+"\n"+"------------\n")
    

def agendaVisita():
    file=open("agendaDia.txt","a") #"a" escribir sin borrarr
    file.close()
    file=open("agendaNoche.txt","a") #"a" escribir sin borrar
    file.close()

    print("--------","\nComplete lo solcitado para agendar una visita 📅")
    turno=int(input("Turno: 1=Diurno ☀️ || 2=Nocturno 🌙: "))
    horario=int(input("Horario 1=Día ☀️ || 2=Noche 🌙:"))
    fecha=input("Fecha: dd/mm/yyyy 📅:  ")
    encargado=input("Nombre de encargado de registro 👤: ")
    print("---------")
    print("Agenda exitosa realizada por el encargado",encargado,"✅")

    if turno==1:
        turno="Diurno ☀️"
        file=open("agendaDia.txt","a") #"a" escribir sin borrar
        file.write("Horario: "+str(horario)+"\n"+"Fecha: "+fecha+"\n"+"Encargado: "+encargado+"\n"+"------------\n")
        file.close()

    else:
        turno="Nocturno 🌙"
        file=open("agendaNoche.txt","a") #"a" escribir sin borrar
        file.write("Horario: "+str(horario)+"\n"+"Fecha: "+fecha+"\n"+"Encargado: "+encargado+"\n"+"------------\n")

def productosNaturales():
    #--pedir datos--
    descripcionProducto=input("Descripción del producto: ")
    cantidadProducto=int(input("Cantidad de producto: "))
    precioProducto=int(input("Precio del producto: "))
    descuento=int(input("Descuento del producto: "))
    #--calculo
    subtotal=cantidadProducto*precioProducto
    descuento2=subtotal-(subtotal*descuento)
    totalGeneral=descuento2+(descuento2*0.13)
    #--factura--
    print("La cantidad de producto es:",cantidadProducto,
        "\nLa descripcion del producto:",descripcionProducto,
        "\nEl precio del producto es:",precioProducto,
        "\n-----FACTURA-----------",
        "\nEl subtotal es:",subtotal,
        "\nEl descuento es:",descuento,
        "\nEl IVA es: 13%",
        "\nEl total general es:",totalGeneral
        )
def verhistorial():
    print("-------------------------")
    
    num=int(input("Ingrese el número de la opción que desea ver: "))
    if num==1:
        file=open("visitantes.txt","r") #"r" leer para lectura
        contenido=file.read()
        print(contenido)
        file.close()
    
#----/LOGIN---/

usuario=""
passw=""
while usuario !="admin" or passw !="admin":
    print("*********************************")
    print("* BIENVENIDO AL PROYECTO 🖥️      *")
    print("* A continuacion digite         *")
    print("* Usuario 🆔 y Contraseña ✳️     *")
    print("*********************************")
    usuario=input("Introduzca su usuario: ")
    passw=input("Introduzca su contraseña: ")
    if usuario=="admin" and passw =="admin":
        print("****************************************************")
        print("*    SELECCIONES LA OPCION QUE DESEE  😎          *")
        print("*    1. VISITANTES 👤                              *")
        print("*    2. AGENDA DE VISITA 📒                        *")
        print("*    3. PRODUCTOS NATURALES 🏞️                      *")
        print("*    4. VER HISTORIAL 📖                           *")
        print("****************************************************")
        tipoReg=int(input("Digite el número de la opción que desea: "))
        if tipoReg==1:
            visitantes()
        elif tipoReg==2:
            agendaVisita()
        elif tipoReg==3:
            productosNaturales()
        elif tipoReg==4:
            verhistorial()
        else:
            print("¡Esta opción no está disponible!")
    else:
        print("Su usuario no fue encontrado")





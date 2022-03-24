#---------------Funciones--------------------------------
def visitantes():
    print("----------------\nComplete lo solicitado:")
    nomCom=input("Nombre completo: ")
    id=int(input("Cédula: "))
    phoneNum=int(input("Número de teléfono: "))
    email=input("Correo electrónico: ")
    address=input("Dirección: ")
    nacionalidad=int(input("Digite si usted es '1.Nacional' o '2.Extrangero': "))
    ageG=int(input("Digite si es 1.Niño, 2.Adulto o 3.Adulto mayor: "))
    print("Registro exitoso para el usuario",nomCom)

def agendaVisita():
    turno=int(input("Turno: 1=Diurno || 2=Nocturno"))
    horario=int(input("Horario 1=Día || 2=Noche: "))
    fecha=input("Fecha: dd/mm/yyyy: ")
    encargado=input("Nombre de encargado de registro: ")

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

#----/LOGIN---/

usuario=""
passw=""
while usuario !="admin" or passw !="admin":
    usuario=input("Introduzca su usuario: ")
    passw=input("Introduzca su contraseña: ")
    if usuario=="admin" and passw =="admin":
        tipoReg=int(input("¿Que quiere registrar? (1=Visitantes||2=Agenda de visita||3=Productos Naturales): "))
        if tipoReg==1:
            visitantes()
        elif tipoReg==2:
            agendaVisita()
        elif tipoReg==3:
            productosNaturales()
        else:
            print("¡Esta opción no está disponible!")
    else:
        print("Su usuario no fue encontrado")





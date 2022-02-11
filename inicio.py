#-----imports------
from modules import funciones

#--Variables
userName = "admin"
password = "admin"


#----bienvenida---
funciones.clearConsole()
print('Bienvenidos a Aguas Termanles Paraiso Azul \n')


#---INICIO DE SESION
if funciones.logueo() == 1:
    print('----------------------------------------------------')
    print('1.Registro        2.Productos Naturales       3.Historial\n4.Salir')
    print('----------------------------------------------------')

    numMenu =input("Seleccione un numero para ingresar al menu:")

    match numMenu:
        case "1":
            print("ESTAMOS EN REGISTRO")
        case "4":
            exit()
        case _:
            print("Digite un numero correto")
            
elif 2 :
    print('chao')







#print(inicioSesion.userName)



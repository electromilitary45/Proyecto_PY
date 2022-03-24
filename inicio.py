#-----imports------
from modules import funciones

#--Variables
userName = "admin"
password = "admin"


#----bienvenida---
funciones.clearConsole()
print('Bienvenidos a Aguas Termales Paraíso Azul \n')


#---INICIO DE SESION
if funciones.logueo() == 1:
    print('----------------------------------------------------')
    print('1.Registro        2.Productos Naturales       3.Historial\n4.Salir')
    print('----------------------------------------------------')

    numMenu =input("Seleccione un número para ingresar al menú:")

    match numMenu:
        case "1":
            print("ESTAMOS EN REGISTRO")
        case "4":
            exit()
        case _:
            print("Digite un número correto")
            
elif 2 :
    print('Chao')







#print(inicioSesion.userName)



#---imports
import os


#--Variables
userName = "admin"
password = "admin"

#---Funcion
def logueo():
    print("Digite sus credenciales")
    userName1=input("Digite su Username: ")
    password1=input("Digite su Password: ")

    if(userName1==userName and password1==password):
        return 1
    elif(userName1!=userName and password1!=password):
        clearConsole()

        print("Tus credenciales son incorrectas!")
        print("Quieres intentarlo otras vez? y/n")
        reintentar=input("")
        if(reintentar=="y" or reintentar=="Y"):
            return logueo()
        elif(reintentar=="n" or reintentar=="N"):
            exit
            
        



#-------Limpiar consola

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

#------


# def logo(userName1):
#     if (userName1 *2):
#         print("hola")

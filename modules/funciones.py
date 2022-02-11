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
        #--Retorna 1 porque es el usuario y contraseña son correctas
        return 1 
    elif(userName1!=userName and password1!=password):
        clearConsole()
        print("Tus credenciales son incorrectas!")
        print("Quieres intentarlo otras vez? y/n")
        reintentar=input("")
        if(reintentar=="y" or reintentar=="Y"):
                    #--Retorna "logueo" porque acepto volver a reinterntar
            return logueo()
        elif(reintentar=="n" or reintentar=="N"):
            #--Retorna 2 porque es el usuario y contraseña son incorrectas
            return 2




#-------Limpiar consola

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)



#--- Salir del programa
def exit():
    command = 'exit'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'exit'
    os.system(command)

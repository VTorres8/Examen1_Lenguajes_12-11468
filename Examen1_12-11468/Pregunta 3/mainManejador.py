import manejador

#Main o menu del manejador de memoria
def menu():
    print("**************************")
    print("***Manejador de Memoria***")
    print("**************************")

    #While true para que se ingrese la cantidad de bloques a manejar y detectar errores de ingresos erroneos
    while True:

        #intentamos recibir la cantidad de bloques por input
        try:
            
            bloques = int(input("Cantidad de bloques de memoria a manejar: "))
            if(bloques >= 1):
                break
            print("OJO: El minimo numero de bloques que puede introducir es 1.\n")

        #Si la cantidad de bloques de memoria a manejar es errada se avisa
        except:
            print("ERROR: Debe introducir un numero valido (entero).\n")

    #Creamos la memoria
    la_memoria = manejador.Memoria(2 ** bloques)

    #While True para introducir la accion que desea realizar y llevar a cabo lo que se pide
    while True:
        opcion = input("*Para reserservar espacio en memoria introduzca, RESERVAR.\n*Para liberar memoria, LIBERAR.\n*Para mostrar el estado de la memoria, MOSTRAR.\n*Si se quiere retirar, SALIR.\n Accion: ")
        
        #Si se va a reservar memoria:
        if opcion.lower() == 'reservar':

            #Si la cantidad de bloques de memoria es invalida se avisa
            try:
                num_bloques = int(input("Cantidad de bloques de memoria a reservar: "))
            
            #Se indica si hay error
            except:
                print("ERROR: Numero de bloques invalido.\n")

            #Se recibe el nombre del identificador
            identificador = input("Ingrese el identificador del programa al que se le reservara la memoria: ")
            la_memoria.agregar(num_bloques, identificador)

        #Si se va a liberar memoria
        elif opcion.lower() == 'liberar':
            identificador = input("Introduzca la identificador del programa a liberar los bloques de memoria: ")
            la_memoria.liberar(identificador)
        
        #Si se va a mostrar la memoria actual
        elif opcion.lower() == 'mostrar':
            la_memoria.mostrar_Memoria(la_memoria.bloque_raiz)

        #Si se va a salir del manejador
        elif opcion.lower() == 'salir':
            break

        #Si se introduce cualquier otra cosa se pide que se ingrese algo valido
        else:
            print("ERROR: Introduzca alguna de las opciones validas.\n")
            

if __name__ == '__main__':
    menu()








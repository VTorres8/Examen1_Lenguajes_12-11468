import sys
from Expresion import *

#Funcion para evaluar la expresion recibida
def evaluar_Expresion(expr):
    #Iniciamos una pila vacia
    pila = []

    #Si la expresion es vacia
    if not expr:
        print("ERROR: No hay expresion que evaluar (es vacia)")

    #Recorremos cada caracter del la expresion
    for caracter in expr:

        #Si es el espacio " ", entonces continuamos recorriendola
        if (caracter == ' '):
            continue
        
        #Si el caracter es un operador ("+","-","*","/")
        elif (caracter=='+' or caracter=='-' or caracter=='*' or caracter=='/'):

            #Try except para sacar el "operando 1" de la pila.
            #En caso de que la pila este vacia, indica error.
            try:
                operando_1 = pila.pop()
            except:  
                return print("ERROR: Faltan operandos para realizar la evaluacion (expresion erronea).")
   
            #Try except para sacar el "operando 2" de la pila.
            #En caso de que la pila este vacia, indica error.
            try:
                operando_2 = pila.pop()
            except:  
                return print("ERROR: Faltan operandos para realizar la evaluacion (expresion erronea).")
            
            #Si el operador era "+", se realiza la suma y se coloca en la pila el resultado
            if(caracter == '+'):
                suma = int(operando_2) + int(operando_1)
                pila.append(suma)

            #Si el operador era "-", se realiza la resta y se coloca en la pila el resultado
            elif(caracter == '-'):
                resta = int(operando_2) - int(operando_1)
                pila.append(resta)

            #Si el operador era "*", se realiza la multiplicacion y se coloca en la pila el resultado
            elif(caracter == '*'):
                mult = int(operando_2) * int(operando_1)
                pila.append(mult)

            ##Si el operador era "/", se realiza la division y se coloca en la pila el resultado
            elif(caracter == '/'):
                div = int(operando_2) // int(operando_1)
                pila.append(div)
        
        #Si el caracter es un operando (un numero), se coloca en la pila
        else:
            pila.append(int(caracter))

    #Al final, quedara el resultado de la evaluacion en la pila y lo extraemos
    resultado = pila.pop()

    #En caso de que llegasen a quedar elementos en la pila, se indica que hubo error con la expresion
    if (pila):
        print("ERROR: Sobraron operandos luego de evaluar (expresion erronea).")
    
    #Se retorna el resultado
    return resultado

#Funcion para obtener el arbol de expresion sufijo (postfijo) de la expresion recibida
def expresion_Sufija(expr, voltear = False):

    #Iniciamos nuestra pila vacia
    pila = []

    #Caso en el que "expr" es vacia
    if not expr:
        return Expresion("")

    #Recorremos cada caracter de la expresion
    for caracter in expr:
        
        #Si es el espacio " ", entonces continuamos recorriendo la expresion
        if (caracter == ' '):
            continue
        
        #Si el caracter es un operador ("+","-","*","/")
        elif (caracter=='+' or caracter=='-' or caracter=='*' or caracter=='/'):

            #Try except para sacar el "operando 1" de la pila.
            #En caso de que la pila este vacia, indica error.
            try:
                operando_1 = pila.pop()
            except:  
                return print("ERROR: Faltan operandos, la expresion no esta bien formada.")
   
            #Try except para sacar el "operando 2" de la pila.
            #En caso de que la pila este vacia, indica error.
            try:
                operando_2 = pila.pop()
            except:  
                return print("ERROR: Faltan operandos, la expresion no esta bien formada.")
   
            #Si voltear es True, pasamos "a" como hijo izquierdo y "b" como hijo derecho de "caracter"
            #(Por lo que volteamos la expresion para obtener la prefija)
            if voltear:
                pila.append(Expresion(caracter,operando_1,operando_2))

            #Si voltear es False, entonces pasamos "b" como hijo izquierdo y "a" como hijo derecho
            # de "caracter", ya que queremos obtener la expresion sufija
            else:
                pila.append(Expresion(caracter,operando_2,operando_1))
        
        #Si el caracter es un numero, lo pasamos como padre sin hijos
        else:  
            pila.append(Expresion(caracter))


    #Si no hay elementos en la pila retorna la expresion vacia
    if not pila:
        return Expresion("")

    #Si hay elemento en la pila retornamos el arbol de Expresion
    arbol_Expresion = pila.pop()

    #Si luego de obtener el arbol quedan cosas en la pila, se indica error
    if pila:
        return print("ERROR: Sobran operandos, la expresion no esta bien formada.")

    return arbol_Expresion

#Fucion para obtener el arbol de expresion Prefijo
def expresion_Prefija(expr):
    #Volteamos la expresion
    expr.reverse()
    return expresion_Sufija(expr, True)

#Funcion para determinar que la expresion ingresada es valida
def expresion_Valida(entrada):

    #Si se ingreso una sola palabra en la entrada y es "SALIDA"
    #Entonces la expresion es valida
    if len(entrada) == 1 and entrada[0] == "SALIR":
        return True

    #Si la entrada tiene menos de 3 elementos
    #o la primera palabra ingresada no es "EVAL" y no es "MOSTRAR"
    #o la segunda palabra ingresada no es "PRE" y no es "POST"
    #Retorna False porque no es valida
    if((len(entrada) < 3) or (entrada[0] != "EVAL" and entrada[0] != "MOSTRAR") or (entrada[1] != "PRE" and entrada[1] != "POST")):
        return False
    
    #Recorremos los caracteres de la entrada a partir de la posicion [2]
    #Es decir, los elementos que conforman la expresion a manejar
    for caracter in entrada[2:]:
        #Si el caracter no es un numero o un operador ("+","-","*","/")
        #Entonces la expresion no es valida
        if(not caracter.isdigit() and caracter != '+' and caracter != '-' and caracter != '/' and caracter != '*'):
            return False

    return True


#Menu de programa por medio del cual se inicia el manejador de expresiones
def menu():
    
    entrada = []

    while(True):

        #Se recibe la entrada de la consola por input
        entrada = input("Introduzca la accion que desea realizar: ").split(' ')

        #Se verifica si el formato de la entrada es valido
        if not expresion_Valida(entrada):
            print("ERROR: Formato de la expresion invalido")
            continue
        
        #Si el comando de entrada es "SALIR" se sale el manejador.
        if entrada[0] == "SALIR":
            break

        arbol_Expresion = None

        #Si la accion es "MOSTRAR":
        if(entrada[0] == "MOSTRAR"):

            #Si el orden es "PRE", se construye el arbol de Expresion Prefijo y, si este
            #no es "None", se "imprime"
            if (entrada[1] == "PRE"):
                arbol_Expresion = expresion_Prefija(entrada[2:])
                if (arbol_Expresion is not None):
                    arbol_Expresion.aExpresion_Infija()

            #Si el orden es "POST", se construye el arbol de Expresion Sufijo y, si este
            #no es "None", se imprime
            else:
                arbol_Expresion = expresion_Sufija(entrada[2:])
                if (arbol_Expresion is not None):
                    arbol_Expresion.aExpresion_Infija()

        #Si la accion es "EVAL":
        else:
            #Si el orden es "PRE" se "voltea" la expresion de entrada, se evalua
            # y se muestra el resultado
            if (entrada[1] == "PRE"):
                expr_volteada = reversed(entrada[2:])
                print(evaluar_Expresion(expr_volteada))
            
            #Si el orden es "POST", se evalua directamente la expresion de entrada
            #y se imprime el resultado
            else:
                print(evaluar_Expresion(entrada[2:]))

if __name__ == "__main__":
    
    menu()
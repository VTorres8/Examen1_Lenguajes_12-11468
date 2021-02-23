#Esta clase modela una expresion recibida como un arbol
class Expresion:
    #Definimos el constructor de la clase, que recibe un "elemento" (elem) de la expresion
    #y sus dos hijos, "izquierdo" y "derecho" respectivamente.
    #En caso de no recibir hijos, entonces los toma como "None" (los ve como vacios).
    def __init__(self, elem, izquierdo = None, derecho = None):
        
        self.elem = elem
        self.izquierdo  = izquierdo 
        self.derecho = derecho

    #Funcion con la que imprimimos el arbol en "Infijo" (InOrder)
    def aExpresion_Infija(self, final = True):

        #Booleano que me indica si el elemento del padre es un operador "*" o "/"
        mult_o_div_padre = self.elem == '*' or self.elem == '/'

        #Recorremos el arbol recursivamente, primero por el hijo izquierdo
        if self.izquierdo is not None:

            #Booleano que me indica si el elemento del hijo izquierdo es un operador "+" o "-"
            suma_o_resta_izq = (self.izquierdo.elem == '+' or self.izquierdo.elem == '-')

            #Si en el "elem" padre tengo una multiplicacion o una division y en el "elem"
            #del hijo izquierdo tengo una suma o una resta, imprimo parentesis para la
            #subexpresion
            if mult_o_div_padre and suma_o_resta_izq:
                print("(", end = "")
            
            self.izquierdo.aExpresion_Infija(False) #Llamada recursiva para seguir imprimiendo el subarbol izq.
            
            if mult_o_div_padre and suma_o_resta_izq:
                print(")", end = "")
        

        #Booleano que me indica si el elemento del padre es un operador (*,/,+,-)
        esOperador = mult_o_div_padre or self.elem == '+' or self.elem == '-'

        #Luego de haber revisado todo el hijo izquierdo (que pudo ser todo un sub arbol de
        #expresiones), imprimimos el "elemento" del padre (del nodo en el que estamos).
        #De esta forma buscamos lograr que, en general los "nodos" del lado izquierdo, y 
        #posteriormente los del lado derecho, esten ubicados e impresos en el lado que les corresponde.
        if esOperador:
            print(" ", end = "")

        print (str(self.elem),end = "")

        if esOperador:
            print(" ", end = "")


        #Ahora procedemos a recorrer recursivamente por el hijo izquierdo
        if self.derecho is not None:

            #Booleano que me indica si el elemento del hijo derecho es un operador "+" o "-"
            suma_o_resta_der = self.derecho.elem == '+' or self.derecho.elem == '-'

            #Booleano que me indica si el elemento del hijo derecho es un operador "*" o "/"
            mult_o_div_der = self.derecho.elem == '*' or self.derecho.elem == '/'

            #Si el padre es una multiplicacion o division y el hijo derecho una suma o resta
            #o Si el  padre es una resta y el hijo derecho es una suma o resta
            #o Si el padre es una division y el hijo derecho es una multiplicacion o division
            #Entonces imprimo parentesis para la subexpresion.

            if (mult_o_div_padre and suma_o_resta_der) or (self.elem == '-' and suma_o_resta_der) or (self.elem == '/' and mult_o_div_der):
                print("(", end = "")

            self.derecho.aExpresion_Infija(False) #Llamada recursiva para seguir imprimiendo el subarbol der.

            if (mult_o_div_padre and suma_o_resta_der) or (self.elem == '-' and suma_o_resta_der) or (self.elem == '/' and mult_o_div_der):
                print(")", end = "")

        #Llegamos al final de la impresion de toda la expresion (el arbol completo)
        if(final):
            return print("\n")

    #Funcion para ver los arboles como string
    def __repr__(self):
        
        hijo_izq = ''
        hijo_der = ''

        #Si hay hijo izquierdo e hijo derecho, los guardo como string
        if(self.izquierdo is not None) and (self.derecho is not None):
            hijo_izq = self.izquierdo.__repr__()
            hijo_der = self.derecho.__repr__()

        #Si no hay hijos simplemente retorno el string de lo que tengo en el elemento padre
        if(hijo_izq == '' and hijo_der == ''):
            return str(self.elem) + " "
        
        #Si tengo hijos imprimo  
        else:    
            return "("+ hijo_izq + str(self.elem) + hijo_der+") "



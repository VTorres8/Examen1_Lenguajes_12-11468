#Clase por medio de la cual definiremos los bloques de memoria modelandolos como los nodos de un arbol
#Con padre, hijos y atributos adicionales
class Bloque:
    def __init__(self,capacidad , padre=None, izq=None, der=None, esta_ocupado = None, identificador = None):
        self.capacidad = capacidad
        self.padre = padre
        self.h_izq = izq
        self.h_der = der
        self.esta_ocupado = esta_ocupado
        self.identificador = identificador

        
#Clase por medio de la cual modelamos todo el espacio de memoria como un gran arbol binario      
class Memoria:
    #Constructor que define como atributos principales la capacidad de la memoria total y el
    #identificador (<nombre>) bajo el que se podra reservar o liberar memoria 
    def __init__(self, capacidad, identificador = None):
        #Como raiz de este "arbol" de memoria tenemos un bloque que contienen la capacidad y el identificador
        #que se menciono antes
        self.bloque_raiz = Bloque(capacidad = capacidad, identificador= identificador )
        #Tendremos el tamano de los bloques
        self.t_bloque = 0
        #Un arreglo donde se manejaran los los nombres/identificadores que se gestionen dentro de la memoria
        self.nombres = []

        #Aplicamos sobre el bloque raiz la funcion "crear_arbMemoria" descrita a continuacion
        self.crear_arbMemoria(self.bloque_raiz) 

    #Funcion por medio de la cual creamos la memoria (modelada como un arbol en esta implementacion)
    #establecemos la capacidad de los bloque hijos en funcion de la capacidad del padre y marcamos sus lazos "filiales"
    #diciendo a los hijos quien es su papa (xd)
    def crear_arbMemoria(self, bloque_Actual): 

        #Si la capacidad del bloque de memoria no es 2 (que sera el menor tamano de bloques de memoria que tendremos puesto que este
        #manejador se base en el "buddy system" y por lo tanto los tamanos de los bloques seran potencias de dos)       
        if(bloque_Actual.capacidad != 2):
            #Entonces a los hijos del bloque actual de memoria les establezco su capacidad como "la capacidad del padre // 2", esto
            #lo hacemos por las razones explicadas anteriormente, necesitamos que los bloques de memoria sean potencias de dos.
            #Adicionalmente indicamos a los bloques hijos que su padre es el bloque actual
            bloque_Actual.h_izq = Bloque(capacidad= bloque_Actual.capacidad //2, padre = bloque_Actual)
            bloque_Actual.h_der = Bloque(capacidad= bloque_Actual.capacidad //2, padre = bloque_Actual)

            #Ahora recursivamente realizamos el proceso antes descrito con todo el hijo izquierdo del bloque de memoria actual
            #y lo mismo con todo su hijo derecho.
            self.crear_arbMemoria(bloque_Actual.h_izq)
            self.crear_arbMemoria(bloque_Actual.h_der)

    #Funcion para insertar bloques de datos en los bloques en memoria
    def insertar(self, capacidad, a_Ocupar, identificador, bloque_Actual, arreglo_disponibles):      
        
        #Si la capacidad del bloque actual es igual a la capacidad del bloque de datos que se quiere insertar y el bloque actual no esta
        #ocupado
        if (bloque_Actual.capacidad == capacidad and not(bloque_Actual.esta_ocupado)):

            #Si el bloqque no es de tamano 2
            if(bloque_Actual.capacidad != 2 ):
                
                #Si el bloque actual no tiene algun hijo ocupado entonces lo insertamos en el arreglo de bloques disponibles
                if not(self.verificar_Algun_Hijo_Ocupado(bloque_Actual)):           
                    arreglo_disponibles.append(bloque_Actual) 
       
            #Si el bloque es de tamano 2 simplemente lo agregamos al arreglo de bloques disponibles
            else:            
                arreglo_disponibles.append(bloque_Actual)   

        #De lo contrario, si la capacidad del bloque no es igual a la del bloque de datos a insertar o si este bloque esta ocupado   
        else:
            #Si el tamano del bloque es distinta de 2 entonces llamamos recursivamente a la funcion de insertar
            #pero esta vez para el hijo izquierdo y el hijo derecho del bloque actual
            if(bloque_Actual.capacidad != 2):
                self.insertar(capacidad, a_Ocupar, identificador, bloque_Actual.h_izq, arreglo_disponibles)       
                self.insertar(capacidad, a_Ocupar, identificador, bloque_Actual.h_der, arreglo_disponibles)

        #Retornamos el arreglo de bloques disponibles
        return arreglo_disponibles

    #Funcion que comprueba el estado de los hijos de un bloque, a diferencia de la anterior no evaluamos con "and" sino con "or"
    #para poder obtener los casos en los que al menos un hijo esta ocupado
    def verificar_Algun_Hijo_Ocupado(self, bloque_Actual): 
        
        #Si el bloque actual no es de tamano 2 entonces
        if(bloque_Actual.capacidad != 2):   

            # Si su hijo izquierdo esta ocupado O si su hijo derecho esta ocupado, retorna true
            if(bloque_Actual.h_izq.esta_ocupado or bloque_Actual.h_der.esta_ocupado):
                return True  

            #De lo contrario, se verifican si algun hijo del hijo izquierdo y el hijo derecho se encuantra ocupado    
            else:
               return self.verificar_Algun_Hijo_Ocupado(bloque_Actual.h_izq) or self.verificar_Algun_Hijo_Ocupado(bloque_Actual.h_der)               
        
        #Si el bloque era de tamano 2, si este esta ocupado se retorna true
        else:            
            if(bloque_Actual.esta_ocupado):
                return True

    #Funcion para ocupar a un bloque y sus hijos
    def ocupar_Bloques(self, bloque_Actual, identificador):

        #Para indicar que esta ocupado colocamos "-1"
        bloque_Actual.esta_ocupado = -1

        #Le asignamos el identificador cuyos datos estan ocupando el bloque
        bloque_Actual.identificador = identificador

        #Si el bloque actual es de tamno 2, como no tiene hijos que ocupar entonces simplemente hacemos return
        #no hay nada mas por hacer
        if bloque_Actual.capacidad == 2:
            return 

        #Llamamos recursivamente para ocupar los bloques en los hijos derecho e izquierdo del bloque actual
        self.ocupar_Bloques(bloque_Actual.h_izq, identificador)
        self.ocupar_Bloques(bloque_Actual.h_der, identificador)


    def agregar(self, aOcupar, etiqueta):        
        return self._agregar(aOcupar, etiqueta)

    #Funcion auxiliar que utilizamos para identificar si se esta tratando de hacer una reserva o insercion validas
    #en memoria y para buscar el best fit en la memoria segun lo indicado por el buddy system
    def _agregar(self, a_Ocupar, identificador):

        #Si la capacidad que se va a ocupar es mayor que la capacidad del bloque raiz de la memoria entonces se indica que se
        #esta excediendo el tamano de memoria disponible
        if(a_Ocupar > self.bloque_raiz.capacidad):
            return print("ERROR: Esta intentando almacenar un bloque de datos mayor al tamano maximo de memoria actual.\n")

        #Si el identificador para el que se esta intentando reservar memoria ya existe en el arreglo de nombres/identificadores
        #en memoria, se indica
        if(identificador in self.nombres):
            return print("ERROR: Identificador ya existente en memoria. \n")
        
        #La capacidad del bloque raiz
        capacidad = self.bloque_raiz.capacidad

        #While True,  capacidad sera igual a la mitad (es decir la capacidad de los hijos)
        #Esto lo hacemos para buscar el best fit como pide el buddy system, dividiendo entre 2 hasta encontrar la capacidad
        #potencia de 2 en la que podamos insertar el bloque de datos deseado.

        #El while se ejecuta hasta que nos encontramos el caso en que:
        #Si la capacidad a ocupar es menor a la capacidad que hemos ido adquiriendo con el while y
        #la capacidad a ocupar es mayor a la capacidad del siquiente bloque de memoria hijo
        #(capacidad del bloque actual //2), entonces nos detenemos ya que hemos hayado el best fit
        
        #se hace break 
        while True:
            if(a_Ocupar <= capacidad and a_Ocupar > capacidad // 2 ):     
                break            
            capacidad = capacidad // 2            
        
        #Si la capacidad del bloque es 1 le sumare 1 puesto que los bloques de menor capacidad son de tamano 2
        if capacidad == 1:
            capacidad += 1       
             
       #Insertamos el bloque de datos en el best fit
        ingresado = self.insertar(capacidad = capacidad, a_Ocupar= a_Ocupar, identificador= identificador, bloque_Actual= self.bloque_raiz, arreglo_disponibles = [])
        
        #Si no se ingreso se indica que hubo un error por no haber suficiente memoria disponible
        if(not(ingresado)):
            print("ERROR: No se pudo ingresar porque no hay suficientes bloques de memoria disponibles.\n")

        #De lo contrario, si se ingreso entonces al primer elemento del arreglo de bloques disponibles obtenido en
        # la variable "ingresado", al que este en la primera posicion lo marcamos ahora como ocupado, le asignamos el identificador
        # correspondiente y agregamos el identificador al arreglo de nombres                             
        else:
            ingresado[0].esta_ocupado = a_Ocupar
            ingresado[0].identificador = identificador
            self.nombres.append(identificador)
            print("BLOQUE INGRESADO CORRECTAMENTE\n")
            
            #Si el bloque ingresado no era de tamano 2, entonces procedemos a marcar sus hijos con el identificador
            #de los datos que se ingresaron
            if(ingresado[0].capacidad != 2):
                self.ocupar_Bloques(ingresado[0].h_izq, identificador)
                self.ocupar_Bloques(ingresado[0].h_der, identificador)

            #Retornamos el bloque ingresado
            return ingresado[0]

    #Funcion para buscar en la memoria todos los bloques que tenian el identificador por el que si liberara memoria
    #para quitarselo
    def buscar_Bloques_A_Liberar(self, identificador, bloque_Actual):      

        #Si el bloque actual no es de tamano 2
        if(bloque_Actual.capacidad != 2):

            #Si el identificador del bloque actual es el que buscamos entonces reemplazamos su identificador con None
            #e indicamos que se encuentra desocupado cambiando su atributo "esta_ocupado" por none
            #Adicionalmente, quitamos el identificador del arreglo de nombres/identificadores de la memoria
            if( bloque_Actual.identificador == identificador):
                bloque_Actual.identificador = None
                bloque_Actual.esta_ocupado = None
                self.nombres.remove(identificador)
                
                #Si el bloque actual no es el bloque raiz y no ocurre que alguno de sus hijos esta ocupado
                #entonces, a su padre le actualizamos el identificador a None y su estado de ocupado a no ocupado (tambien poniendo none)
                if(bloque_Actual != self.bloque_raiz and not(bloque_Actual.padre.h_der.esta_ocupado or bloque_Actual.padre.h_izq.esta_ocupado)):
                    
                    bloque_Actual.padre.identificador = None
                    bloque_Actual.padre.esta_ocupado = None
            
                ##Luego procedemos a liberar los hijos izquierdo y derecho del bloque actual
                self.liberar_Bloques_Hijos(bloque_Actual.h_izq)
                self.liberar_Bloques_Hijos(bloque_Actual.h_der)

                #Retornamos true al terminar
                return True

            #Si el bloque actual no tiene el identificador que buscamos entronces procedemos a llamar recursivamente  la funcion de busqueda
            #sobre su hijo izquierdo y derecho y retornamos true si alguno fue liberado del identificador
            else:
                return self.buscar_Bloques_A_Liberar(identificador, bloque_Actual.h_izq) or self.buscar_Bloques_A_Liberar(identificador, bloque_Actual.h_der)
        
        #Si el bloque es de tamano 2
        else:
            #Si el bloque actual tiene el identificador, lo libero como se hizo anteiormente
            if(bloque_Actual.identificador == identificador):
                self.nombres.remove(identificador)
                bloque_Actual.identificador = None
                bloque_Actual.esta_ocupado = None
                
                #Si para el bloque padre del bloque actual, no ocrre que alguno de sus hijos este ocupado
                #entonces libero al bloque padre del identificador y cambio su estado a no ocupado tambien con None
                if(not(bloque_Actual.padre.h_der.esta_ocupado or bloque_Actual.padre.h_izq.esta_ocupado)):
                    
                    bloque_Actual.padre.identificador = None
                    bloque_Actual.padre.esta_ocupado = None
                
                #retornamos true al terminar
                print("BLOQUE LIBERADO CON EXITO\n")
                return True      
    
    #Funcion para liberar los bloques hijos
    def liberar_Bloques_Hijos(self, bloque_Actual):
        
        #Al bloque actual le 
        bloque_Actual.esta_ocupado = None
        bloque_Actual.identificador = None
        
        if bloque_Actual.capacidad == 2:
            return 

        self.liberar_Bloques_Hijos(bloque_Actual.h_izq)
        self.liberar_Bloques_Hijos(bloque_Actual.h_der)

    #Funcion auxiliar para liberar con la que verificamos si el identificador que queremos liberar
    #esta en el arreglo de nombre/identificadores en memoria, si no esta se avisa
    #Luego de la verificacion  llamamos a la funcion de buscar bloques a liberar
    def liberar(self, identificador):
        if not(identificador in self.nombres):
            return print("ERROR: El identificador que quiere liberar no existe en memoria\n")
        return self.buscar_Bloques_A_Liberar(identificador, self.bloque_raiz)
    

    #Funcion para mostrar en consola el "arbol" de memoria
    def mostrar_Memoria(self, bloque_Actual, nivel = 0, direccion = None):

        #Si nos encontramos en el bloque raiz, entonces:
        if bloque_Actual == self.bloque_raiz:

            #Si  el bloque esta ocupado entonces lo imprimo con sus especificaciones de capacidad
            if(bloque_Actual.esta_ocupado != None):
                print(f"*Bloque padre*; Capacidad: {bloque_Actual.capacidad}; Bloques Ocupados: {bloque_Actual.esta_ocupado}.")

            #sino, procedemos a mostrar los hijos del bloque actual
            elif(self.verificar_Ambos_Hijos_Ocupados(bloque_Actual)):
                print(f"*Bloque padre*: 'AMBOS BLOQUES HIJOS OCUPADOS' ")  
            
            #Sino, si el bloque padre esta libre se muestra dicha informacion
            else:
                print(f"*Bloque padre*; Capacidad: {bloque_Actual.capacidad}; OJO: Todavia hay bloques libres.")

            #Ahora el padre del bloque raiz es el actual
            self.bloque_raiz.padre = bloque_Actual  

        #Si no estamos en un bloque raiz:    
        else: 
            #Pequeno ciclo para manejar tabs  
            for i in range(nivel):
                print("\t",end="")
            
            #Si el bloque actual esta ocupado (para saberlo le habremos colocado -1 en el momento de su ocupacion)
            if(bloque_Actual.esta_ocupado == -1):
                print(f"Bloque con: Capacidad: {bloque_Actual.capacidad}; Con *Bloque Padre* ocupado por identificador: {bloque_Actual.identificador} (id en el actual); Identificador en bloque padre: {bloque_Actual.padre.identificador}; Capacidad del padre: {bloque_Actual.padre.capacidad}; Este bloque es hijo {direccion}", end="")

            #Si el bloque actual tiene hijos que mostrar y su capacidad no es 2 (minima capacidad de bloque que hay) y el identificador en el bloque actual no esta en el arreglo de nombres/identificadores
            elif(self.verificar_Ambos_Hijos_Ocupados(bloque_Actual) and bloque_Actual.capacidad != 2 and not(bloque_Actual.identificador in self.nombres)):
                print(f"Bloque con: Capacidad: {bloque_Actual.capacidad}; OJO: AMBOS HIJOS OCUPADOS; Identificador en Bloque Padre: {bloque_Actual.padre.identificador}; Capacidad del padre: {bloque_Actual.padre.capacidad}. Este bloque es hijo {direccion}", end="")
            
            #Si el bloque actual no esta ocupado
            elif(bloque_Actual.esta_ocupado == None):

                #Si es un bloque "hoja", es decir de tamano 2 (de menor capacidad en toda la memoria)
                if(bloque_Actual.capacidad == 2):
                    print(f"Bloque con: Capacidad:  {bloque_Actual.capacidad}; OJO: AUN HAY BLOQUES LIBRES; Identificador en Bloque Padre: {bloque_Actual.padre.identificador}; Capacidad del padre: {bloque_Actual.padre.capacidad}. Este bloque es hijo {direccion}", end="")
                
                #Si no es un bloque de tamano 2
                else:           
                    print(f"Bloque con: Capacidad:  {bloque_Actual.capacidad}, OJO: AUN HAY BLOQUES LIBRES; Identificador en Bloque Padre: {bloque_Actual.padre.identificador}; Capacidad del padre: {bloque_Actual.padre.capacidad}. Este bloque es hijo {direccion}", end="")
            
            #En caso de que no se ninguno de los bloques anteriores
            else:
                print(f"Bloque con: Capacidad:  {bloque_Actual.capacidad}; Ocupados: {bloque_Actual.esta_ocupado} bloques de datos con identificador: {bloque_Actual.identificador}. Identificadore del bloque padre: {bloque_Actual.padre.identificador}; Capacidad del padre: {bloque_Actual.padre.capacidad}. Este bloque es hijo {direccion}", end="")
            print("\n")
        
        #Si no es un bloque "hoja" de tamano 2
        if (bloque_Actual.capacidad != 2):

            #Procedemos a correr recursivamente la funcion mostrar con el hijo izquierdo y con el hijo derecho
            self.mostrar_Memoria(bloque_Actual.h_izq, nivel + 1, 'izquierdo')
            self.mostrar_Memoria(bloque_Actual.h_der, nivel + 1, 'derecho')

    #Funcion para verificar el estado de los hijos de un bloque (casos en los que ambos esta ocupados)
    def verificar_Ambos_Hijos_Ocupados(self, bloque_Actual): 
        
        #Si el bloque actual no es de tamano 2
        if(bloque_Actual.capacidad != 2):  

            #Si su hijo izquierdo e hijo derecho estan ocupados, retorna True  
            if(bloque_Actual.h_izq.esta_ocupado and bloque_Actual.h_der.esta_ocupado):
                return True   

            #Si no estan ocupados procede a comprobar el estado de los hijos tanto del hijo izquierdo
            #como del derecho y retorna true si para cada para de hijos respectivamente, su estado es ocupado             
            else:
               return self.verificar_Algun_Hijo_Ocupado(bloque_Actual.h_izq) and self.verificar_Algun_Hijo_Ocupado(bloque_Actual.h_der)

        #Si el bloque es de tamano 2, si esta ocupado retorna true            
        else:            
            if(bloque_Actual.esta_ocupado):
                return True
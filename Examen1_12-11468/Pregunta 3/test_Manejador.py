import manejador
import unittest

class Test_Manejador(unittest.TestCase):

    #Creamos una instancia de Memoria
    def test_Bloque(self):
        bloque = manejador.Bloque(32)
        self.assertIsInstance(bloque, manejador.Bloque)

   #Creamos una instancia de Memoria
    def test_Memoria(self):
        la_memoria = manejador.Memoria(16)
        self.assertIsInstance(la_memoria, manejador.Memoria)

    #Probamos mostar memoria
    def test_mostrar_Memoria(self):
        la_memoria = manejador.Memoria(16)
        la_memoria.mostrar_Memoria(la_memoria.bloque_raiz)
        print("\n\n")
    
    #Mostrar la memoria con solo un ocupado
    def test_mostrar_Memoria2(self):
        la_memoria = manejador.Memoria(8)
        la_memoria.agregar(1,'ID1')
        la_memoria.mostrar_Memoria(la_memoria.bloque_raiz)
        print("\n\n")
    
    #Verificar si algun hijo del arbol esta ocupado luego de crearlo
    def test_verificar_Algun_Hijo_Ocupado(self):
        la_memoria = manejador.Memoria(32)
        self.assertIsNone(la_memoria.verificar_Algun_Hijo_Ocupado(la_memoria.bloque_raiz))

    #Probar si hay un bloque ocupado luego de agregar 
    def test_verificar_Algun_Hijo_Ocupado2(self):
        la_memoria = manejador.Memoria(32)
        la_memoria.agregar(3, 'Identificador')
        self.assertTrue(la_memoria.verificar_Algun_Hijo_Ocupado(la_memoria.bloque_raiz))

    #Probar insertar un bloque con mayor capacidad a la actual en memoria
    def test_Pasandose_de_Memoria(self):
        la_memoria = manejador.Memoria(16)        
        self.assertIsNone(la_memoria.agregar(20, 'EPA! qlq!'))

    #Probar agregar un identificador que ya existe
    def test_agregar_Id_Existente(self):
        la_memoria = manejador.Memoria(16)
        la_memoria.agregar(1, 'ENTRO')
        self.assertIsNone(la_memoria.agregar(2,'ENTRO'))

    #Probar liberar bloques
    def test_liberar(self):
        la_memoria = manejador.Memoria(8)
        la_memoria.agregar(2, 'ID1')
        la_memoria.agregar(2, 'ID2')
        self.assertTrue(la_memoria.liberar('ID1'))
        self.assertTrue(la_memoria.liberar('ID2'))

    #Probar que se libero una etiueta recien agregada
    def test_agregar_liberar(self):
        la_memoria = manejador.Memoria(32)
        la_memoria.agregar(3,'ID1')
        la_memoria.liberar('ID1')
        self.assertFalse('id1' in la_memoria.nombres)
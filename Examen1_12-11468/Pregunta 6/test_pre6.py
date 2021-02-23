from pre6 import *
from unittest import TestCase
from io import StringIO
from unittest.mock import patch
import os
import subprocess

#Clase para realizar pruebas
class pre6_Test(TestCase):

    #Probar funcion "aExpresion_Infija" de la clase "Expresion" cumple su funcion (y retorna none al final)
    def test_aExpresion_Infija(self):

        arbExpr = Expresion('/',Expresion('-',Expresion('10'),
                                            Expresion('1')),  Expresion('*', Expresion('1'),
                                                                            Expresion('3')))
        salida = arbExpr.aExpresion_Infija()
        self.assertIsNone(salida)

    #Probar la funcion "evaluar" con una Expresion "PRE"
    def test_evaluar_expresion_PRE(self):
        entrada = reversed("+ * + 3 4 5 7")
        salida = evaluar_Expresion(entrada)
        resultado = 42
        self.assertEqual(salida, resultado)

    #Probar la funcion "evaluar" con una Expresion "POST"
    def test_evaluar_expresion_POST(self):
        entrada = "8 3 - 8 4 4 + * +"
        salida = evaluar_Expresion(entrada)
        resultado = 69
        self.assertEqual(salida, resultado)

    #Probar la funcion "evaluar" con una Expresion erronea
    def test_evaluar_expresion_ERROR(self):
        entrada = "8 - 3"
        salida = evaluar_Expresion(entrada)
        resultado = None #Porque la expresion esta mal formada
        self.assertIsNone(salida, resultado)

    #Probar que para una expresion valida dada, "expresion_Prefija" no me da vacia
    def test_expresion_Prefija(self):

        expr = ['+','14','3']

        salida = expresion_Sufija(expr)
        self.assertNotEqual(salida, [])

    #Probar que a nivel de una representacion en string, la "expresion_Prefija"
    #genera el arbol deseado
    def test_representacion_expresion_Prefija(self):

        expr = ['*','10','5']
        resultado = Expresion('*',Expresion('10'),Expresion('5'))

        salida = expresion_Prefija(expr)
        self.assertEqual(repr(salida), repr(resultado))

    #Probar que a nivel de una representacion en string, la "expresion_Sufija"
    #genera el arbol deseado
    def test_representacion_expresion_Sufija(self):

        expr = ['3','8','-']
        resultado = Expresion('-',Expresion('3'),Expresion('8'))

        salida = expresion_Sufija(expr)
        self.assertEqual(repr(salida), repr(resultado))
    
    #Probar que para una expresion valida dada,"expresion_Sufija", no me da vacia
    def test_expresion_Sufija(self):

        expr = ['3','8','-']

        salida = expresion_Sufija(expr)
        self.assertNotEqual(salida, [])

    #Probar "expresion_Valida" para verificar el formato de la entrada
    #Caso invalido con 1 elemento en la entrada:
    def test_expresion_Valida_Fallo1(self):

        expr = ['Soy uno pero no soy Salida jeje...']

        salida = expresion_Valida(expr)

        self.assertFalse(salida)

    #Caso invalido con menos de 3 elementos en la entrada
    def test_expresion_Valida_Fallo2(self):

        expr = ['UNO', 'DOS']

        salida = expresion_Valida(expr)

        self.assertFalse(salida)

    #Caso invalido con 3 elementos en la entrada
    def test_expresion_Valida_Fallo3(self):

        expr = ['UNO', 'DOS', 'TRES pollito ingles']

        salida = expresion_Valida(expr)

        self.assertFalse(salida)
    
    #Prueba para menu, con un input mocked. Corre y compara el resultado correctamente pero
    #La prueba arroja un pequeno error luego del chequeo porque side_effect funciona como un
    #iterador y causa problema al detenerse
    entrada = 'EVAL PRE + * + 3 4 5 7'
    @patch('builtins.input', side_effect=[entrada])
    def test_sum_string_of_ints(self, mock_input):
        self.assertEqual(menu(), 42)


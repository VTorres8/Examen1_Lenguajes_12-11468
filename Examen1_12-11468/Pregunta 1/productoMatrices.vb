'Función para producto de Funciones en VB.NET'

'Recibe la matriz A de dimension (NxM) y la matriz B de dimension (MxP)'
Public Function Producto(ByVal A(,) As Decimal, ByVal B(,) As Decimal) As Decimal(,)

 

            'Comprobamos que las matrices, para poder ser multiplicadas, cumplen con el requisito de que
            'el numero de columnas de la primera debe ser igual al numero de filas de la segunda
            'para esto escribimos que si el indice mas alto de la segunda dimension de la matriz (A.GetUpperBound(1))
            'no es igual al indice mas alto de la primera dimension de la segunda matriz (B.GetupperBound(0))
            'entonces se sale de la funcion

            If A.GetUpperBound(1) <> B.GetUpperBound(0) Then

                 Exit Function

            End If

 

            Dim i, j, k As Short

            'Si se cumple el requisito, procedemos a crear la matriz producto
            'Cuyas dimensiones son el numero de filas de la matriz A (A.GetUpperBound(0))
            'y el numero de columnas de la matriz B (B.GetUpperBound(1))

            Dim R(A.GetUpperBound(0), B.GetUpperBound(1)) As Decimal

 

            'Creamos un array de dos columnas que usaremos para operar entre los elementos
            'de las matrices para tener por ejemplo:
            'A(1,0) * B(0 ,0)
            'A(1,1) * B(1 ,0)
            'A(1,2) * B(2 ,0)

            Dim T(A.GetUpperBound(1), 1) As Decimal

 

            'Luego, con los siguientes dos ciclos For iremos visitando todas las
            'posiciones de la matriz producto R (el primer For se pasea por las filas
            'y el segundo por las columnas)

            For i = 0 To R.GetUpperBound(0)

                For j = 0 To R.GetUpperBound(1)

 

                    'Aqui, i contiene el primer índice de R, que vamos a colocar en todas las
                    'posiciones A(i, ) de los elementos de la primera matriz.
                    'Y, a la vez, en la segunda posción A( ,k) vamos aumentando el índice
                    'desde cero hasta el número de columnas de A (que coincide con el de
                    'filas de B)

                    For k = 0 To A.GetUpperBound(1)

                        T(k, 0) = A(i, k)

                    Next

 

                    'Y j contiene el segundo índice de la matriz producto R, que colocamos en todas
                    'las posiciones B(,j) de los elementos de la segunda matriz.
                    'Y, a la vez, en la primera posción B(k, ) vamos aumentando el índice desde cero
                    'hasta el número de filas de B (que coincide con el de columnas de A)

                    For k = 0 To B.GetUpperBound(0)

                        T(k, 1) = B(k, j)

                    Next

 

                    'De esta manera ya tenemos definidos todos los elementos que necesitamos.
                    'Nos queda multiplicar cada pareja del array T e ir acumulando los
                    'resultados (sumando) para luego colocar el resultado final en su respectiva
                    'posicion de la matriz producto R. Basicamente vamos construyendo por ejemplo:
                    'A(1,0) * B(0 ,0) + A(1,1) * B(1 ,0) + A(1,2) * B(2 ,0)... y asignandolo en la
                    'matriz R en la posicion que le corresponde.


                    For k = 0 To T.GetUpperBound(0)

                        R(i, j) += T(k, 0) * T(k, 1)

                    Next

 

                Next

            Next

            'Al final solo debemos retornar la matriz producto resultante, R

            Return R

 

End Function

'Queda simplemente plantear las matrices A y B y probar la funcion producto
Private Sub Prueba_de_producto()

        Dim A(,) As Decimal = {{1, 2, 3}, {3, 2, 1}}

        Dim B(,) As Decimal = {{1, 2}, {3, 1}, {2, 1}}

        Dim R(,) As Decimal = Producto(A, B)
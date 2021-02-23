'Funcion para calcular el factorial de un n dado
Public Function Factorial(n As Integer)

    'Tenemos la variables n y fact del tipo Integer'
    Dim i As Integer
    Dim fact As Integer

    'Si el numero n, es cero entonces su factorial da 1'
    If n = 0 Then
        fact = 1

    'De lo contrario se calcula el factorial
    Else
        For i = 1 To n
            fact = fact * i
        Next

    End If

    Return fact
End Function
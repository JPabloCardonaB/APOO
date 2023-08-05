"""
Escribir una función que calcule el factorial de un número dado.
"""

def calcular_factorial(numero):

    numero_factorial = numero

    for i in range(numero - 1, 0, -1):
        numero_factorial = numero_factorial * i

    return(numero_factorial)    


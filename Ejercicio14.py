"""
Escribir una función que calcule la media aritmética de una lista de números.
"""

def calcular_media_aritmetica(lista):
    media_aritmetica = 0
    
    for i in range(len(lista)):
        media_aritmetica += i

    return media_aritmetica


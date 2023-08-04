"""
Crear una función que invierta el orden de los elementos en una lista dada.
"""

def invertir_lista(lista_bacana):
    lista_invertida = []
    indice = len(lista_bacana) - 1

    while(indice >= 0):
        lista_invertida.append(lista_bacana[indice])
        indice -= 1

    return lista_invertida

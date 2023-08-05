"""
Crear un programa que genere una lista de números aleatorios y los imprima en pantalla.
"""

def main():
    import random

    tamaño_lista = int(input("Ingrese el tamaño de la lista: "))
    lista_numeros = []

    for i in range(tamaño_lista):
        lista_numeros.append(random.randint(0, 100))

    print(lista_numeros)

main()
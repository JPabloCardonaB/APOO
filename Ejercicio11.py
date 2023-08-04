"""
Crear un programa que genere una lista de números pares entre 1 y 100
"""

def main():
    import random

    tamaño_lista = random.randint(0, 100)
    lista_bacana= []

    for i in range(tamaño_lista):
        lista_bacana.append(random.randint(0, 100))

    print(lista_bacana)
main()
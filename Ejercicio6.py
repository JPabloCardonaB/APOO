"""
Crear un programa que calcule la suma de los números en una lista dada
"""

def main():

    lista_bacana = [1,2,3,4,5,6,7,8,9]
    suma_numeritos = 0

    for i in range(len(lista_bacana)):
        suma_numeritos += lista_bacana[i]

    print(suma_numeritos)

main()
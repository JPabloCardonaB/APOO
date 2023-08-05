"""
Escribir un programa que encuentre el número más grande y el más pequeño en una lista dada.
"""

def main():

    lista_bacana = [2, 5, 4, 3, 1, 9]
    numero_menor = 999
    numero_mayor = 1

    for i in range(len(lista_bacana)):
        if lista_bacana[i] > numero_mayor:
            numero_mayor = lista_bacana[i]
    print(f"el numero mayor es: {numero_mayor}")

    for i in range(len(lista_bacana)):
        if lista_bacana[i] < numero_menor:
            numero_menor = lista_bacana[i]
    print(f"el numero menor es: {numero_menor}")


main()
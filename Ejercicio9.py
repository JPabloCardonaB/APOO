"""
Crear un programa que genere una matriz de números y la imprima en pantalla.
"""
def crear_matriz(fil, col, mat):
    import random

    for f in range(fil):
        for c in range(col):
            mat[f][c] = random.randint(0, 100)

def mostrar_matriz(fil, col, mat):
    for f in range(fil):
        for c in range(col):
            print(mat[f][c], end = "\t")
        print("\n")

def main():
    import random

    filas = random.randint(0, 6)
    columnas = random.randint(0, 6)
    matriz = []
    for f in range(filas):
        matriz.append([0]* columnas) 

    crear_matriz(filas, columnas, matriz)
    mostrar_matriz(filas, columnas, matriz)
main()
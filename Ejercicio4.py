"""
Escribir un programa que determine si un número dado es par o impar
"""

def main():

    numero = int(input("Ingrese un numero entero: "))

    if numero % 2 == 0:
        print(f"el numero {numero}, es par")
    else:
        print(f"el numero {numero}, es impar")

main()
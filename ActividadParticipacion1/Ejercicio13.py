"""
Crear un programa que pida al usuario ingresar dos números y calcule su suma, resta, multiplicación y
división.
"""

def main():

    numero_1 = int(input("Hola!, Ingresa un numero por favor: "))
    numero_2 = int(input("Ahora ingresa otro numero por favor: "))

    suma = numero_1 + numero_2
    resta = numero_1 - numero_2
    multiplicacion = numero_1 * numero_2
    divison = numero_1 / numero_2

    print(f"El resultado de la suma de los dos numeros es: {suma}, la resta es: {resta}, la multiplicacion es: {multiplicacion}, la division es: {divison}")
main()
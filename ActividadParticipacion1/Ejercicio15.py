"""
Crear un programa que pida al usuario ingresar una cadena de texto y determine si es un palíndromo o no.
"""

def es_palindromo(cadena):
    
    cadena = cadena.replace(" ", "").lower()
    
    return cadena == cadena[::-1]

def main():
    # Pedimos al usuario que ingrese la cadena de texto
    texto = input("Ingresa una cadena de texto: ")

    if es_palindromo(texto):
        print("Es un palíndromo.")
    else:
        print("No es un palíndromo.")

main()


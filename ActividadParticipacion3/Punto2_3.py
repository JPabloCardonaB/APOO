"""
Cree una clase Punto que represente un punto en el plano cartesiano
"""
import math
class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def imprimir_coordenadas(self):
        print(f"Las coordenadas son: x = {self.x}, y= {self.y}")

    def cambiar_coordenadas(self, nueva_x, nueva_y):
        self.x = nueva_x
        self.y = nueva_y

    def calcular_distancia_puntos(punto1, punto2):
        distancia = math.sqrt((punto2.x - punto1.x) ** 2 + (punto2.y - punto1.y) ** 2)       
        return distancia
            

punto1 = Punto(3, 1)
punto2 = Punto(2, 5)

#mover coordenadas

#print("coordenadas originales")
#punto1.imprimir_coordenadas()
#punto1.cambiar_coordenadas(5, 5)
#print("Coordenadas nuevas")
#punto1.imprimir_coordenadas()

print(Punto.calcular_distancia_puntos(punto1, punto2))


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

    def calcular_distancia_puntos(self, punto2):
        distancia = math.sqrt((punto2.x - self.x) ** 2 + (punto2.y - self.y) ** 2)       
        return distancia
            

punto1 = Punto(3, 0)
punto2 = Punto(9, 0)

#mover coordenadas
print("coordenadas originales")
punto1.imprimir_coordenadas()
punto1.cambiar_coordenadas(5, 0)
print("Coordenadas nuevas")
punto1.imprimir_coordenadas()

print(punto1.calcular_distancia_puntos(punto2))


"""
Cree una clase Circulo que tenga las propiedades centro y radio, las cuales se inicializan con parámetros en el constructor.
Defina métodos en la clase para calcular el área, el perímetro e indicar si un punto pertenece al círculo o no.
"""
import math

class Circulo():
    def __init__(self, centro, radio):
        self.centro = centro
        self.radio = radio

    def area_circulo(self):
        return math.pi * self.radio ** 2
    
    def perimetro_circulo(self):
        diametro = self.radio * 2
        perimetro = diametro * math.pi

        return perimetro

    def comprobar_pertenencia_punto(self, punto):
        
        distancia_centro_punto = math.sqrt((punto.x - self.centro.x) ** 2 + 
                                            (punto.y - self.centro.y) ** 2) 
           
        if distancia_centro_punto <= self.radio:
            return "El punto pertenece al circulo"
        else:
            return "El punto no pertenece al circulo"


class Punto():
    def __init__(self, x, y):
        self.x = x
        self.y = y 


centro = Punto(0, 0)
circulo = Circulo(centro, 2)
punto1 = Punto(1, 1)

print(f"El area del circulo es: {circulo.area_circulo()}")
print(f"El perimetro del cirullo es: {circulo.perimetro_circulo()}")
print(f"{circulo.comprobar_pertenencia_punto(punto1)}")
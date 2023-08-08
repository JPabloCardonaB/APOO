"""
Cree una clase Rectángulo la cual contiene
dos atributos de instancia que representan los puntos que definen sus esquinas. Agregue métodos a la claseRectángulo 
para calcular su perímetro, calcular su área e indicar si el rectángulo es un cuadrado.
"""
import math

class Rectangulo():
    def __init__(self, punto1, punto2, punto3, punto4):
        self.punto_esquina_1 = punto1
        self.punto_esquina_2 = punto2        
        self.punto_esquina_3 = punto3
        self.punto_esquina_4 = punto4

    def calcular_perimetro(self):     
        distancia_punto1_punto2 = math.sqrt((self.punto_esquina_2.x - self.punto_esquina_1.x) ** 2 + 
                                            (self.punto_esquina_2.y - self.punto_esquina_1.y) ** 2)    
           
        distancia_punto1_punto3 = math.sqrt((self.punto_esquina_3.x - self.punto_esquina_1.x) ** 2 + 
                                            (self.punto_esquina_3.y - self.punto_esquina_1.y) ** 2)
        
        perimetro = (distancia_punto1_punto2 * 2) + (distancia_punto1_punto3 * 2)
        return perimetro
    
    def calcular_area(self):
        distancia_punto1_punto2 = math.sqrt((self.punto_esquina_2.x - self.punto_esquina_1.x) ** 2 + 
                                            (self.punto_esquina_2.y - self.punto_esquina_1.y) ** 2)    
           
        distancia_punto1_punto3 = math.sqrt((self.punto_esquina_3.x - self.punto_esquina_1.x) ** 2 + 
                                            (self.punto_esquina_3.y - self.punto_esquina_1.y) ** 2)
        
        area = distancia_punto1_punto2 * distancia_punto1_punto3
        return area

    def comprobar_cuadrado(self):
        distancia_punto1_punto2 = math.sqrt((self.punto_esquina_2.x - self.punto_esquina_1.x) ** 2 + 
                                            (self.punto_esquina_2.y - self.punto_esquina_1.y) ** 2)    
           
        distancia_punto1_punto3 = math.sqrt((self.punto_esquina_3.x - self.punto_esquina_1.x) ** 2 + 
                                            (self.punto_esquina_3.y - self.punto_esquina_1.y) ** 2)
    
        if distancia_punto1_punto2 == distancia_punto1_punto3:
            return "cuadrado"
        else:
            return "rectangulo"
        
class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

punto1 = Punto(1, 1)
punto2 = Punto(11, 1)
punto3 = Punto(1, 4)
punto4 = Punto(11, 4)

rectangulo = Rectangulo(punto1, punto2, punto3, punto4)

print(f"el perimetro es: {rectangulo.calcular_perimetro()}")
print(f"el area del rectangulo es: {rectangulo.calcular_area()}")
print(f"las coordenadas corresponden a un: {rectangulo.comprobar_cuadrado()}")
"""
Cree una clase Rectángulo la cual contiene
dos atributos de instancia que representan los puntos que definen sus esquinas. Agregue métodos a la claseRectángulo 
para calcular su perímetro, calcular su área e indicar si el rectángulo es un cuadrado.
"""

class Rectangulo():
    def __init__(self, punto1, punto2):
        self.punto_esquina_1 = punto1
        self.punto_esquina_2 = punto2        

    def calcular_perimetro(self):     
        distancia_lado_mayor = self.punto_esquina_2.x - self.punto_esquina_1.x
        distancia_lado_menor = self.punto_esquina_2.y - self.punto_esquina_1.y               
        perimetro = abs((distancia_lado_menor * 2) + (distancia_lado_mayor * 2))
        return perimetro
    
    def calcular_area(self):
        distancia_lado_mayor = self.punto_esquina_2.x - self.punto_esquina_1.x
        distancia_lado_menor = self.punto_esquina_2.y - self.punto_esquina_1.y
        
        area = abs(distancia_lado_mayor * distancia_lado_menor)
        return area

    def comprobar_cuadrado(self):
            
        distancia_lado_mayor = self.punto_esquina_2.x - self.punto_esquina_1.x
        distancia_lado_menor = self.punto_esquina_2.y - self.punto_esquina_1.y

        if  distancia_lado_menor == distancia_lado_mayor: 
            return "cuadrado"
        else:
            return "rectangulo"
        
class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

punto1 = Punto(8, 2)
punto2 = Punto(14, 4)

rectangulo = Rectangulo(punto1, punto2)

print(f"el perimetro es: {rectangulo.calcular_perimetro()}")
print(f"el area del rectangulo es: {rectangulo.calcular_area()}")
print(f"las coordenadas corresponden a un: {rectangulo.comprobar_cuadrado()}")
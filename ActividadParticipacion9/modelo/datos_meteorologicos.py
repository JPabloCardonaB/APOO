class DatosMeteorologicos:

    def __init__(self, nombre_archivo: str):
        self.nombre_archivo: str = nombre_archivo

        self.sumar_temperaturas = 0
        self.cantidad_de_temperaturas = 0
        self.temperatura_promedio = 0

        self.sumar_humedades = 0
        self.cantidad_de_humedades = 0
        self.humedad_promedio = 0

        self.sumar_presiones = 0
        self.cantidad_de_presiones = 0
        self.presion_promedio = 0

        self.sumar_velocidades_del_viento = 0
        self.cantidad_de_velocidades_del_viento = 0
        self.velocidad_del_viento_promedio = 0

        self.suma_de_direcciones_del_viento = 0
        self.cantidades_de_direcciones_del_viento = 0
        self.direccion_del_viento_promedio = 0

    def procesar_datos(self) -> tuple[float, float, float, float ,str]:
        with open(self.nombre_archivo, "r") as archivo:
            for linea in archivo:
                if "Temperatura" in linea:
                    temperatura_promedio = self.calcular_temperatura_promedio(linea)
                if "Humedad" in linea:
                    humedad_promedio = self.calcular_humedad_promedio(linea)
                if "Presion" in linea:
                    presion_promedio = self.calcular_presion_promedio(linea)
                if "Viento" in linea:
                    velocidad_del_viento_promedio, direccion_del_viento_promedio = self.calcular_velocidad_promedio_del_viento(linea)
            direccion_viento_str = self.convertir_direccion_float_a_str(self.direccion_del_viento_promedio)
            print("Los datos han sido procesado con exito")
        return (temperatura_promedio, humedad_promedio, presion_promedio, velocidad_del_viento_promedio, direccion_viento_str)

    def calcular_temperatura_promedio(self, linea: str) -> float:
        temperatura = float(linea.split(':')[1].strip())
        self.sumar_temperaturas += temperatura
        self.cantidad_de_temperaturas += 1
        self.temperatura_promedio = self.sumar_temperaturas / self.cantidad_de_temperaturas
        return self.temperatura_promedio

    def calcular_humedad_promedio(self, linea: str) -> float:
        humedad = float(linea.split(':')[1].strip())
        self.sumar_humedades += humedad
        self.cantidad_de_humedades += 1
        self.humedad_promedio = self.sumar_humedades / self.cantidad_de_humedades
        return self.humedad_promedio

    def calcular_presion_promedio(self, linea: str) -> float:
        presion = float(linea.split(':')[1].strip())
        self.sumar_presiones += presion
        self.cantidad_de_presiones += 1
        self.presion_promedio = self.sumar_presiones / self.cantidad_de_presiones
        return self.presion_promedio
        
    
    def calcular_velocidad_promedio_del_viento(self, linea: str) -> float:
        velocidad_del_viento = linea.split(':')[1].strip()
        velocidad_del_viento = float(velocidad_del_viento.split(',')[0].strip())
        self.sumar_velocidades_del_viento += velocidad_del_viento
        self.cantidad_de_velocidades_del_viento += 1
        self.velocidad_del_viento_promedio = self.sumar_velocidades_del_viento/self.cantidad_de_velocidades_del_viento

        direcciones_del_viento: dict[str:int] = {"N":0,
                                     "NNE":22.5,
                                     "NE":45,
                                     "ENE":67.5,
                                     "E":90,
                                     "ESE":112.5,
                                     "SE":135,
                                     "SSE":157.5,
                                     "S":180,
                                     "SSW":202.5,
                                     "SW":225,
                                     "WSW":247.5,
                                     "W":270,
                                     "WNW":292.5,
                                     "NW":315,
                                     "NNW":337.5
            }
        direccion_del_viento = linea.split(":")[1].strip()
        direccion_del_viento = direccion_del_viento.split(",")[1].strip()

        for claves in direcciones_del_viento.keys():
            if direccion_del_viento == claves:
                self.suma_de_direcciones_del_viento += direcciones_del_viento[claves]
                self.cantidades_de_direcciones_del_viento += 1
        self.direccion_del_viento_promedio = self.suma_de_direcciones_del_viento/self.cantidades_de_direcciones_del_viento
        return self.velocidad_del_viento_promedio, self.direccion_del_viento_promedio
        

    def convertir_direccion_float_a_str(self,direccion_del_viento_promedio : float)-> str:
        direcciones_del_viento: dict[str:int] = {"N":0,
                                     "NNE":22.5,
                                     "NE":45,
                                     "ENE":67.5,
                                     "E":90,
                                     "ESE":112.5,
                                     "SE":135,
                                     "SSE":157.5,
                                     "S":180,
                                     "SSW":202.5,
                                     "SW":225,
                                     "WSW":247.5,
                                     "W":270,
                                     "WNW":292.5,
                                     "NW":315,
                                     "NNW":337.5
            }
        cantidad_cercana_al_promedio_str = ''

        for claves in direcciones_del_viento.keys():
            if direccion_del_viento_promedio < direcciones_del_viento[claves]:
                cantidad_cercana_al_promedio_str = claves
                break 

        return cantidad_cercana_al_promedio_str
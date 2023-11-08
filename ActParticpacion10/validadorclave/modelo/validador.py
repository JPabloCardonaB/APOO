# TODO: Implementa el código del ejercicio aquí
from abc import ABC, abstractmethod
from validadorclave.modelo.errores import *


class ReglaValidacion(ABC):

    def __init__(self, longitud_esperada: int):
        self.longitud_esperada:int = longitud_esperada

    def validar_longitud(self, clave:str) -> bool:

        if len(clave) > self.longitud_esperada:
            return True
          
        raise NoCumpleLongitudMinimaError(f" la clave '{clave}' no tiene la longitud esperada: {self.longitud_esperada}")
    
    def contiene_mayuscula(self, clave:str) -> bool:

        for letra in clave:
            if letra.isupper():
                return True     
            else:  
                raise NoTieneLetraMayusculaError(f"La clave '{clave}' no tiene ninguna letra mayuscula")

    def contiene_minuscula(self, clave:str) -> bool:
        
        for letra in clave:
            if letra.islower():
                return True
            else:
                raise NoTieneLetraMinusculaError(f"la clave '{clave}' no tiene ninguna letra minuscula")
            
    def contiene_numero(self, clave:str) -> bool:   
        
        for numero in clave:
            if numero.isdigit():
                return True
            else:
                raise NoTieneNumeroError(f"La clave '{clave}' no tiene ningun numero")
            
    @abstractmethod
    def es_valida(clave:str):        
        pass

class Validador(ReglaValidacion):

    def __init__(self, longitud_esperada: int, regla: ReglaValidacion):
        self.regla = regla

    def es_valida(self, clave: str) -> bool:
        return self.regla.es_valida(clave) 
         
class ReglaValidacionGanimedes(ReglaValidacion):

    def __init__(self, longitud_esperada: int):
        super().__init__(longitud_esperada)

    def contiene_caracter_especial(self, clave:str):

        for caracter_especial in clave:
            if caracter_especial == "@":
                return True
            if caracter_especial == "_":
                return True
            if caracter_especial == "#":
                return True
            if caracter_especial == "$":
                return True
            if caracter_especial == "%":
                return True
            else:
                False
        raise NoTieneCaracterEspecialError(f"La clave '{clave}' no contiene ningun caracter especial @, _, #, $, %")
    
    def es_valida(self, clave: str) -> bool:
        
        longitud = self.validar_longitud(clave)
        mayusculas = self.contiene_mayuscula(clave)
        minusculas = self.contiene_minuscula(clave)
        numero = self.contiene_numero(clave)
        caracter_especial = self.contiene_caracter_especial(clave)
        
        if longitud  == True and mayusculas == True and minusculas == True and numero == True and caracter_especial == True:
            return True
        else:
            raise ValidadorError(f"la clave '{clave}' no cumple la validacion Ganimedes")


class ReglaValidacionCalisto(ReglaValidacion):

    def __init__(self, longitud_esperada: int):
        super().__init__(longitud_esperada)

    def contiene_calisto(self, clave:str) -> bool:
        clave_en_minuscula = clave.lower()
        posicion_de_calisto = clave_en_minuscula.find("calisto")
        contador_de_mayusculas = 0
        posicion_final_calisto = posicion_de_calisto + 7

        for letra in range(posicion_de_calisto, posicion_final_calisto):
            if clave[letra].isupper():
                contador_de_mayusculas += 1
        if contador_de_mayusculas >= 2 and contador_de_mayusculas <7:
            return True
        else:
            raise NoTienePalabraSecretaError(f"la clave '{clave}' no tiene la palabra secreta: calisto")
        
    def es_valida(self, clave: str) -> bool:
        
        longitud = self.validar_longitud(clave)
        numero = self.contiene_numero(clave)
        contiene_calisto = self.contiene_calisto(clave)

        if longitud == True and numero == True and contiene_calisto == True:
            return True
        else:
            raise ValidadorError(f"La clave '{clave}' no cumple la validacion Calisto")
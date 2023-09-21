from dataclasses import dataclass, field

@dataclass
class Elemento:
    nombre: str = ""

    def _eq_(self, other: str) -> bool:
        if self.nombre == other.nombre:
            return True
        else:
            return False
        
class Conjunto:
    contador:int = 0

    @classmethod
    def intersectar(cls, conjunto1, conjunto2):
        conjunto1.lista_objetos + conjunto2.lista_objetos
        
        
    def _init_(self, nombre_conjunto: str):
        self.lista_objetos: list[Elemento] = []
        self.nombre_conjunto: str = nombre_conjunto 
        Conjunto.contador += 1
        self.__id = Conjunto.contador

        @property
        def id(self):
            return self.__id
   
    def contiene(self, objeto: Elemento) -> bool:
        for elemento in self.lista_objetos:
            if elemento == objeto:
                return True
        return False

    def agregar_elemento(self, objeto:Elemento):
        if self.contiene(objeto) == False:
            self.lista_objetos.append(objeto)

    def _add_(self, other):
        AuB = self.unir(other)
        return AuB

    def unir(self, other):
        AuB = Conjunto( { f" {self.nombre_conjunto} UNIDO {other.nombre_conjunto}"})
        for elemento in self.lista_objetos:
            AuB.agregar_elemento(elemento)
        for elemento in other.lista_objetos:
            AuB.agregar_elemento(elemento)
        return AuB
    
    def _str_(self):
        elementos_str = ', '.join(elemento.nombre for elemento in self.lista_objetos)
        return f"{self.nombre_conjunto}: ({elementos_str})"
    
    @classmethod
    def intersectar(cls, conjunto, conjunto2):
        nuevo_conjunto = Conjunto( { f" {conjunto.nombre_conjunto} INTERSECTADO {conjunto2.nombre_conjunto}"})
        for i in conjunto.lista_objetos:
            for j in conjunto2.lista_objetos:
                if i == j:
                    nuevo_conjunto.agregar_elemento(j)
        return nuevo_conjunto    


conjunto1 = Conjunto("Fulbo1")
conjunto2 = Conjunto("Fulbo2")

elemento1 = Elemento("Messi")
elemento2 = Elemento("Moises Gaicedo")
elemento3 = Elemento("Cetre")
elemento4 = Elemento("Cristiano")
elemento5 = Elemento("Jarlan")
elemento6 = Elemento("FalcaGOD")

conjunto1.agregar_elemento(elemento1)
conjunto1.agregar_elemento(elemento2)
conjunto1.agregar_elemento(elemento3)
conjunto1.agregar_elemento(elemento4)
conjunto2.agregar_elemento(elemento5)
conjunto2.agregar_elemento(elemento6)
conjunto2.agregar_elemento(elemento1)
conjunto2.agregar_elemento(elemento4)

print(conjunto1)
print(conjunto2)
print(Conjunto.intersectar(conjunto1, conjunto2))
print(conjunto1 + conjunto2)
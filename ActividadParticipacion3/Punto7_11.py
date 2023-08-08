"""
Cree una clase CuentaBancaria que contenga los siguientes atributos: numero_cuenta, propietarios y balance. 
Los tres atributos se deben inicializar en el constructor con valores recibidos como parámetros.
Para la clase CuentaBancaria, cree un método depositar que maneje las acciones de depósito en la cuenta.
Para la clase CuentaBancaria, cree un método retirar que maneje las acciones de retiro de la cuenta.
Para la clase CuentaBancaria, cree un método aplicar_cuota_manejo que aplique un porcentaje del 2% sobre el balance de la cuenta
Para la clase CuentaBancaria, cree un método mostrar_detalles que imprima por consola los detalles de la cuenta bancaria.
"""

class CuentaBancaria():

    def __init__(self, numero_cuenta, propietarios, balance):

        self.numero_cuenta = numero_cuenta
        self.propietarios = propietarios
        self.balance = balance

    def depositar(self, cantidad_deposito):
        if cantidad_deposito > 0:
            self.balance = cantidad_deposito
            print("El deposito se ha realizado correctamente!!")
        else:
            print("No se ha podido encontrar el numero de la cuenta, rectifique la informacion e intentelo nuevamente")
    
    def retirar_dinero(self, cantidad_retiro):
        if cantidad_retiro > 0:
            self.balance -= cantidad_retiro
            print("se ha realizado el retiro correctamente!!!")
        else:
            print("La cantidad a retirar no es valida")

    def aplicar_cuota_manejo(self):
        self.balance -= self.balance * 0.02
        print(f"Se ha realizado el cobro de la cuota de manejo a su cuenta, ahora su balance es de: {self.balance}")

    def mostrar_detalles_cuenta(self):

        print(f"----------Los detalles de la cuenta son:-----------")
        print(f"el numero de su cuenta es: {self.numero_cuenta}")
        print(f"El propietario de la cuenta es: {self.propietarios}")
        print(f"el balance de la cuenta es: {self.balance}$")

cuenta_bancaria = CuentaBancaria(20092005,"Pablo",0)

cuenta_bancaria.depositar(1000000)
print(f"El balance de la cuenta es: {cuenta_bancaria.balance}")

cuenta_bancaria.retirar_dinero(10000)
print(f"El balance de la cuenta es: {cuenta_bancaria.balance}")

cuenta_bancaria.aplicar_cuota_manejo()
cuenta_bancaria.mostrar_detalles_cuenta()
        


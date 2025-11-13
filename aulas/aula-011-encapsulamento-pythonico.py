import stdiomask

class Conta:
    def __init__(self, titular, saldo, pin):
        self.__titular = titular
        self.__saldo = saldo
        self.__pin = pin
        self.__limite = 400
      
    @property  
    def saldo(self):
        if self.valida_pin():
            return self.__saldo
        
    @saldo.setter
    def saldo(self, valor):
        if self.valida_pin():
            self.__saldo += valor
        
    def valida_pin(self):
        confirma_pin = input('Digite o pin: ')
        if confirma_pin == self.__pin:
            return True
        else:
            return False

# INICIO DO PROGRAMA           

nova_conta = Conta('Ricardo', 5000, stdiomask.getpass('Pin: ', '*'))

print(nova_conta.saldo)

nova_conta.saldo = 500

print(nova_conta.saldo)
import stdiomask

class Conta:
    def __init__(self, titular, saldo, pin):
        self.__titular = titular
        self.__saldo = saldo
        self.__pin = pin
        self.__limite = 400
        
    def get_saldo(self):
        confirma_pin = input('Digite o pin: ')
        
        if confirma_pin == self.__pin:
            return self.__saldo
        else:
            return None
        
    
    def set_pin(self):
        
        confirma_pin = input('Digite o pin antigo: ')
        if confirma_pin == self.__pin:
            novo_pin = input('Digite o novo pin: ')
            confirma_novo_pin = input('Confirme o novo pin: ')
            
            if novo_pin == confirma_novo_pin:
                self.__pin = novo_pin
        
    
    def levantamento(self, valor):
        confirma_pin = stdiomask.getpass('Digite o pin: ', '*')
        if confirma_pin == self.__pin:
            if valor <= self.__limite:
                self.__saldo -= valor
                print(f'{valor:.2f}€ retirados com sucesso')
                print(f'Novo saldo: {self.__saldo:.2f}€')
            else:
                print(f'Ultrapassou os {self.__limite:.2f}€')  
        else:
            print('Pin Inválido')
            

# INICIO DO PROGRAMA           

nova_conta = Conta('Ricardo', 5000, stdiomask.getpass('Pin: ', '*'))

nova_conta.set_pin()
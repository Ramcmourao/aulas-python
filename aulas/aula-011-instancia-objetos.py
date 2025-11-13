import stdiomask

class Conta:
    def __init__(self, titular, saldo, pin):
        self.titular = titular
        self.saldo = saldo
        self.pin = pin
        self.limite = 400
        
    def levantamento(self, valor):
        confirma_pin = stdiomask.getpass('Digite o pin: ', '*')
        if confirma_pin == self.pin:
            if valor <= self.limite:
                self.saldo -= valor
                print(f'{valor:.2f}€ retirados com sucesso')
                print(f'Novo saldo: {self.saldo:.2f}€')
            else:
                print(f'Ultrapassou os {self.limite:.2f}€')  
        else:
            print('Pin Inválido')
            
            
nova_conta = Conta('Ricardo', 5000, '1234')

print(nova_conta.saldo)

nova_conta.levantamento(int(input('Digite o valor a levantar: ')))

nova_conta.saldo += 5000000000

print(nova_conta.saldo)
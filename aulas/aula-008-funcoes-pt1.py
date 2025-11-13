import os

def limpa_ecra():
    os.system('cls')
    
    
def separador():
    print('-----------------')


def cabecalho(msg):
    separador()
    print(f'--- {msg} ---')
    separador()
    
    
def tabuada(numero):
    for c in range(0, 10):
        print(f'{numero} x {c+1} = {numero*(c+1)}')


def soma(num1, num2):
    print(f'{num1} + {num2} = {num1 + num2}')


def contador(*num):
    soma = 0
    
    for numero in num:
        soma += numero
        
    print(f'A soma dos valores é: {soma}')


def mostra_lista(lista):
    for numero in lista:
        print(f'-> {numero}')

limpa_ecra()
#contador(1, 2, 3)
#contador(1, 3, 4, 5, 8, 9)
#contador(3)

valores = [1, 3, 5, 7, 10, 15]

mostra_lista(valores)



#cabecalho('Tabuada')
#num = int(input('Digite um número: '))
#tabuada(num)
#soma(5, 5, 5)

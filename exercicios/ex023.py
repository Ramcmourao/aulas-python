'''
Crie um programa que leia vários números inteiros e que termine apenas quando o utilizador digitar a opção para parar. No final mostre quantos números o utilizador inseriu, qual a soma entre eles e qual o maior e menor número inserido.
'''
import os

os.system('cls')

contador = soma = maior = menor = 0

print('--- ANÁLISE DE VALORES ---')

while True:
    numero = int(input('Digite um número [0 para parar]: ')) # pede um valor
    
    if numero == 0: # se esse valor for zero o programa termina
        break
    
    if contador == 0: #verifica se é o primeiro valor a ser inserido
        maior = menor = numero # inicia maior e menor com o primeiro valor inserido
    else:
        if numero > maior: # se o valor inserido for superior ao valor em maior
            maior = numero # maior recebe esse novo valor
        elif numero < menor: # se o valor inserido for inferior ao valor de menor
            menor = numero # menor recebe esse novo valor

    contador += 1 # incrementa o contador
    soma += numero # soma o novo valor
    
# Apresenta os resultados
print(f'Inseriu {contador} números.')
print(f'A soma é: {soma}.')
print(f'O maior valor inserido foi: {maior}')
print(f'O menor valor inserido foi: {menor}')

        
    
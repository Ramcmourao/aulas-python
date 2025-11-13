'''
Faça um programa que leia um número
inteiro e diga se ele é ou não um
número primo.
'''

import os

os.system('cls')

numero = int(input('Digite um número: '))
contador_restos = 0

for c in range(1, numero + 1):
    if numero % c == 0:
        contador_restos += 1
    
    if contador_restos > 2: # Sempre que o contador de restos for superior a 2 já sabemos que o número NÃO É PRIMO
        break # então o programa faz um break no for, ou seja, quebra o ciclo e sai do loop

if contador_restos == 2:
    print(f'O número {numero} É PRIMO')
else:
    print(f'O número {numero} NÃO É PRIMO')
    

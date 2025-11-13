'''Faça um programa que leia 5 números
inteiros e mostre a soma desses
números.'''

import os

os.system('cls')

soma = 0

for c in range(0, 5):
    numero = int(input(f'Digite o {c+1}º número: '))
    soma += numero
    
print(f'A soma dos números é {soma}')

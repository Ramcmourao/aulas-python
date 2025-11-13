'''
Crie um programa que crie uma matriz 3x3 e preencha com valores lidos pelo teclado. No final mostre a matriz com a formatação adequada.
'''

matriz = list()
temp = list()

for linha in range(0, 3):
    for coluna in range(0, 3):
        valor = int(input('Digite um valor: '))
        temp.append(valor)
    matriz.append(temp[:])
    temp.clear()

for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'{matriz[linha][coluna]}', end=' ')
    print()
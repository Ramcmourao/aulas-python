'''
A soma de todos os valores pares.
A soma dos valores da segunda coluna.
O maior valor da terceira linha.
'''
from random import randint

matriz = list()
temp = list()

soma_pares = 0
soma_coluna_dois = 0

# É o que faz a leitura
for linha in range(0, 3):
    for coluna in range(0, 3):
        valor = randint(0, 9)
        
        # soma dos valores pares
        if valor % 2 == 0:
            soma_pares += valor
        
        # soma valores segunda coluna
        if coluna == 1:
            soma_coluna_dois += valor
            
        # maior da terceira linha
        if linha == 2:
            if coluna == 0:
                maior = valor
            else:
                if valor > maior:
                    maior = valor
        
        temp.append(valor)
    matriz.append(temp[:])
    temp.clear()

# Apenas mostra valores
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'{matriz[linha][coluna]}', end=' ')
    print()
    
print(f'\nA soma dos valores pares é {soma_pares}.')
print(f'A soma dos valores da segunda coluna é {soma_coluna_dois}')
print(f'O maior valor da terceira linha é {maior}')
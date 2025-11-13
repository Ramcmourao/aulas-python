'''

Crie um programa que tenha uma função que receba 3 parâmetros: inicio, fim e passo. O programa deve realizar 3 contagens através da função.

De 1 até 20, de 2 em 2
De 10 até 0, de 1 em 1
Contagem personalizada


'''

def contagem(inicio, fim, passo):
    if passo <= 0:
        passo = 1
        print('Passo alterado para 1.')
    
    if inicio < fim:   
        for c in range(inicio, fim+1, passo):
            print(c)
    else:
        passo = -passo
        for c in range(inicio, fim, passo):
            print(c)
        

contagem(1, 20, 2)
contagem(10, 0, 1)

i = int(input('Digite o inicio: '))
f = int(input('Digite o fim: '))
p = int(input('Digite o passo: '))

contagem(i, f, p)
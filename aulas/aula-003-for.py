# O range dentro do ciclo for pede 2 parametros obrigatórios
# range(inicio, fim)

# O passo é opcional
# range(inicio, fim, passo)

'''
numero = int(input('Digite um número: '))

print('COM O FOR')
for c in range(0, 10):
    print(f'{numero} x {c + 1} = {numero*(c + 1)}')
'''

'''soma = 0

fim = int(input('Quantas notas vai inserir: '))

for c in range(0, fim):
    nota = float(input('Digite uma nota: '))
    
    soma = soma + nota
    
print(soma / fim)'''

'''from time import sleep
import os

for c in range(10, 0, -1):
    os.system('cls')
    print(c)
    sleep(1)
    
print('Feliz ano 2026')

string = 'Está tudo cheio de sono.'

for c in range(0, len(string)):
    if string[c] == 'á':
        print(string[c])
        print(c)
'''

inicio = int(input('Digite o inicio: '))
fim = int(input('Digite o fim: ')) + 1
passo = int(input('Digite o passo: '))

for c in range(inicio, fim, passo):
    print(c)
import os
os.system('cls')

print('--- MENU ---')
print('[ 1 ] - Calculadora')
print('[ 2 ] - Tabuada')
print('[ 3 ] - Números pares')
print('[ 4 ] - Sair')

opcao = int(input('--> '))

if opcao == 1:
    print('Escolheu calculadora')
    
elif opcao == 2:
    os.system('cls') # limpa o terminal
    print('--- Tabuada ---')
    
    numero = int(input('Digite um número: '))
    
    print(f'{numero} x 1 = {numero * 1}')
    print(f'{numero} x 2 = {numero * 2}')
    print(f'{numero} x 3 = {numero * 3}')
    print(f'{numero} x 4 = {numero * 4}')
    print(f'{numero} x 5 = {numero * 5}')
    print(f'{numero} x 6 = {numero * 6}')
    print(f'{numero} x 7 = {numero * 7}')
    print(f'{numero} x 8 = {numero * 8}')
    print(f'{numero} x 9 = {numero * 9}')
    print(f'{numero} x 10 = {numero * 10}')
    
elif opcao == 3:
    os.system('cls')
    print('--- Números Pares ---')
    
    numero = int(input('Digite um número: '))
    
    if numero % 2 == 0:
        print(f'O número {numero} é PAR.')
    else:
        print(f'O número {numero} é IMPAR.')
    
elif opcao == 4:
    print('Sair...')

else:
    print('Escolheu uma opção inválida.')
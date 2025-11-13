'''contador = 1
while contador <= 5:
    print(contador)
    contador += 1'''

import os
opcao = ''

while opcao != 4:
    os.system('cls')
    
    print('--- MENU ---')
    print('[ 1 ] - Calculadora')
    print('[ 2 ] - Números primos')
    print('[ 3 ] - Números Pares')
    print('[ 4 ] - Sair')
    opcao = int(input('---> '))
    
    if opcao == 1:
        print('Escolheu calculadora')
    elif opcao == 2:
        print('Escolheu números primos')
    elif opcao == 3:
        print('Escolheu números pares')
    elif opcao == 4:
        print('Escolheu sair...')
        
    _ = input('ENTER para continuar...')
    
print('Programa terminado')
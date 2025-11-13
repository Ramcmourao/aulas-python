'''
Crie o seguinte menu:

--- Calculadora ---
[ 1 ] - Tabuada
[ 2 ] - Calculadora
[ 3 ] - Números Pares
[ 4 ] - Sair

Mediante a opção solicitada o sistema deve executar a ação do menu.
'''

import os # importa a biblioteca OS

os.system('cls') # Função que limpa o terminal

# Apresenta o menu
print('--- Calculadora ---')
print('[ 1 ] - Tabuada')
print('[ 2 ] - Calculadora')
print('[ 3 ] - Números Pares')
print('[ 4 ] - Sair')
opcao = int(input('--> ')) # lê a opção do utilizador

if opcao == 1:
    os.system('cls') # limpa o terminal
    print('--- Tabuada ---') # apresenta um titulo
    numero = int(input('Digite um número: ')) # pede um número ao utilizador
    
    # sequencia de prints que mostram a tabuada
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

elif opcao == 2:
    os.system('cls') # limpa o terminal
    print('--- Calculadora ---') # apresenta um titulo
    
    expressao = input('--> ') # lê a expressão para calcular
    
    # identifica os índices das operações para poder fatiar a expressão
    indice_mais = expressao.find('+')
    indice_menos = expressao.find('-')
    indice_multiplicar = expressao.find('x')
    indice_dividir = expressao.find('/')
    
    # Caso os índices sejam identificados escolhe qual a operação a ser feita
    # Se o índice tiver o valor -1 significa que não encontrou o operador
    # Caso seja diferente de -1 então é o valor do índice
    if indice_mais != -1:
        num1 = int(expressao[:indice_mais]) # Do índice zero até ao indice do operador é o primeiro número ou numeros
        num2 = int(expressao[indice_mais+1:]) # Do índice do operador +1 é o segundo número ou numeros
        print(num1 + num2)
        
    elif indice_menos != -1:
        num1 = int(expressao[:indice_menos]) # Do índice zero até ao indice do operador é o primeiro número ou numeros
        num2 = int(expressao[indice_menos+1:]) # Do índice do operador +1 é o segundo número ou numeros
        print(num1 - num2)
    
    elif indice_multiplicar != -1:
        num1 = int(expressao[:indice_multiplicar]) # Do índice zero até ao indice do operador é o primeiro número ou numeros
        num2 = int(expressao[indice_multiplicar+1:]) # Do índice do operador +1 é o segundo número ou numeros
        print(num1 * num2)
        
    elif indice_dividir != -1:
        num1 = int(expressao[:indice_dividir]) # Do índice zero até ao indice do operador é o primeiro número ou numeros
        num2 = int(expressao[indice_dividir+1:]) # Do índice do operador +1 é o segundo número ou numeros
        if num2 == 0: # faz uma pequena validação para evitar erros de divisão por zero
            print('ERRO DIVISÃO POR ZERO')
        else:
            print(num1 / num2)

elif opcao == 3:
    os.system('cls') # limpa o terminal
    print('--- Números Pares ---') # mostra o titulo
    
    numero = int(input('Digite um número: ')) # pede um numero ao utilizador
    
    if numero % 2 == 0: # se o resto da divisão for zero é PAR
        print(f'O número {numero} é PAR')
    else:
        print(f'O número {numero} é ÍMPAR')
        
elif opcao == 4:
    print('A sair...')
    
else: # valida apenas opções inválidas
    print('Opção inválida.') 
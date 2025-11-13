'''
Crie um programa com uma função chamada fatorial(), que receba dois parâmetros: o primeiro será o número a calcular o fatorial e o segundo será opcional e lógico que indique se será exibido no ecrã ou não o processo de cálculo do fatorial.
'''

def fatorial(numero, mostra=False):
    '''
    -> Calcula o fatorial de um número com a possibilidade de mostrar o processo.
    :param numero: O valor usado para o fatorial
    :param mostra: Boolean para mostrar ou não o processo
    return: sem retorno
    '''
    from math import factorial
    
    if numero < 0:
        print('Não é possível calcular o fatorial de valores negativos.')
        return
    
    if type(numero) == float:
        print('Não é possível calcular o fatorial de valores não inteiros.')
        return
        #print(f'A calcular o fatorial como {int(numero)}')
        #numero = int(numero)
    
    if not mostra:
        print(f'O fatorial de {numero} é {factorial(numero)}')
    else:
        print(f'{numero} x ', end='')
        
        for c in range(numero-1, 0, -1):
            if c == 1:
                print(f'{c} = {factorial(numero)}')
            else:
                print(f'{c} x ', end='')
                
                
#num = int(input('Digite um número para calcular o seu fatorial: '))
#exibe = True if int(input('Mostrar cálculo?\n[ 1 ] - Sim\n[ 2 ] - Não\n--> ')) == 1 else False

fatorial(4.5, True)
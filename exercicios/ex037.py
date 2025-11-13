'''
Escreva um programa que peça ao utilizador para inserir dois números e divida o primeiro pelo segundo. Utilize o tratamento de exceções para lidar com casos em que o segundo número é zero e quando a entrada não é um número válido.
'''

try:
    num1 = int(input('Digite um número: '))
    num2 = int(input('Digite outro número: '))

    divisao = num1 / num2
    
    #soma = num1 + str(num2) typeError
    
except ZeroDivisionError:
    print('Não é possível dividir por ZERO.')
    
except ValueError:
    print('O utilizador não digitou um número.')
    
except TypeError:
    print('Não é possível soma um inteiro com String')
    
else:
    print(f'{num1} / {num2} = {divisao}')
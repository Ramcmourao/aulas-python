'''
Cria um programa que leia 2 valores introduzidos pelo utilizador e que apresente a sua SOMA, SUBTRAÇÃO, MULTIPLICAÇÃO, DIVISÃO e RESTO.
'''

num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))

soma = num1 + num2
subtracao = num1 - num2
multiplicacao = num1 * num2
divisao = num1 / num2
resto = num1 % num2

print(soma)
print(subtracao)
print(multiplicacao)
print(int(divisao))
print(resto)
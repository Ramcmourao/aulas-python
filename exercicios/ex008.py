'''
Cria um programa que leia 5 notas introduzidas pelo utilizador e que calcule a média aritmética entre eles.
'''
import time

nota1 = float(input('Digite a 1ª nota: '))
nota2 = float(input('Digite a 2ª nota: '))
nota3 = float(input('Digite a 3ª nota: '))
nota4 = float(input('Digite a 4ª nota: '))
nota5 = float(input('Digite a 5ª nota: '))

media = (nota1 + nota2 + nota3 + nota4 + nota5) / 5

print('A calcular média', end='', flush=True)
time.sleep(1)
print('.', end='', flush=True)
time.sleep(1)
print('.', end='', flush=True)
time.sleep(1)
print('.', flush=True)
time.sleep(1)

print('A média é:', media, 'valores.')
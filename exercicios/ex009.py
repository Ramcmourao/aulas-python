'''
Crie um programa que pergunte a quantidade de km percorridos por um carro alugado e quantidade de dias que foi alugado. Apresente o total a pagar sabendo que o carro custa 60€/dia e 0.456€/km.
'''
from time import sleep
import os

os.system('cls')

CUSTO_DIA = 60
CUSTO_KM = 0.456

print('--- RENTA CAR ---')

sleep(1)

qtd_km = float(input('Digite quantos kms percorreu: '))
qtd_dias = int(input('Digite quantos dias esteve alugado: '))

preco = CUSTO_DIA * qtd_dias + CUSTO_KM * qtd_km

sleep(1)
print('A calcular...')
sleep(1)

print('Total a pagar:', preco, '€.')

import os
from time import sleep
import random

os.system('cls')

print('-----------------------------')
print('--- JOGO DA ADIVINHA V1.0 ---')
print('-----------------------------')

sleep(1)

_ = input('Clique ENTER para continuar...')

os.system('cls')

print('Pensei num número entre 0 e 7...')
print('Achas que consegues adivinhar?')

aleatorio = random.randint(0, 7)
palpite = int(input('--> '))

print('A analisar...')
sleep(1)

if palpite == aleatorio:
    print('PARABÉNS!')
    print(f'Eu escolhi o número {aleatorio} e tu o {palpite}.')
else:
    print('NÃO GANHOU!')
    print(f'Eu escolhi o número {aleatorio} e tu o {palpite}.')
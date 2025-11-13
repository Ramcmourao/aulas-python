'''
Crie o jogo da adivinha v2.0. O computador deve “pensar” num número de 0 a 10 e o utilizador deve adivinhar o número escolhido. Só que agora o jogador vai tentar adivinhar até acertar. A cada tentativa, o programa deve informar se é “mais acima” ou “mais abaixo”. No final mostre quantas tentativas foram necessárias.
'''

from random import randint
import os

os.system('cls')

# defino as variáveis iniciais
ALEATORIO = randint(0, 50) # valor aleatorio
tentativa = '' # variavel para o while funcionar
contador = 0

print('-----------------------------')
print('--- JOGO DA ADIVINHA V2.0 ---')
print('-----------------------------\n')

print('Pensei num número entre 0 e 50...')
print('Consegues adivinhar???')

while tentativa != ALEATORIO:
    tentativa = int(input('--> '))
    contador += 1
    
    if tentativa > ALEATORIO:
        print('Mais abaixo...')
    elif tentativa < ALEATORIO:
        print('Mais acima')
        
print(f'Acertaste. Pensei no {ALEATORIO} e jogaste {tentativa}.')
print(f'Número de tentativas: {contador}')
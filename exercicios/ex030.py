'''
Cria um programa que crie palpites para o Euromilhões. O programa deve perguntar quantas chaves serão geradas e deve sortear aleatoriamente 5 números de 1 a 50 [sem repetir] e 2 estrelas de 1 a 12 [sem repetir]. Cada sorteio deve ser guardado numa lista composta.
'''
from random import randint
import os
from time import sleep

os.system('cls')

print('--- GERADOR DE CHAVES PARA O EUROMILHÕES ---')

palpites = []
quantas = int(input('Quantas chaves deseja gerar?\n-->'))

for c in range(quantas):
    numeros = []
    estrelas = []
    
    # gerar 5 números
    while len(numeros) < 5:
        numero = randint(1, 50)
        if numero not in numeros:
            numeros.append(numero)
    
    # gerar 2 estrelas
    while len(estrelas) < 2:
        estrela = randint(1, 12)
        if estrela not in estrelas:
            estrelas.append(estrela)
    
    palpite = {
        'numeros': numeros,
        'estrelas': estrelas
    }
    
    palpites.append(palpite)

print('\n=== CHAVES GERADAS ===')

for indice, palpite in enumerate(palpites):
    print(f'Chave {indice+1}:')
    
    for num in palpite['numeros']:
        print(f'| {num} ', end='', flush=True)
        sleep(0.5)
        
    for est in palpite['estrelas']:
        print(f'| *{est} ', end='', flush=True)
        sleep(0.5)
    
    print('\n')

print('Boa sorte!')
        
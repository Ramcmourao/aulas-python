'''
Faça um programa que leia uma frase
qualquer e diga se é um palíndromo,
desconsiderando os espaços.
Ex: Anotaram a data da maratona
'''

import os

os.system('cls')

frase = input('Digite uma frase: ').replace(' ', '').lower()

frase_inversa = frase[::-1]

palindromo = True

for c in range(0, len(frase)):
    if frase[c] != frase_inversa[c]:
        palindromo = False
    
if palindromo: # é o mesmo que -> if palindromo == True:
    print('A frase inserida é um Palindromo')
else:
    print('A frase inserida NÃO é um Palindromo')
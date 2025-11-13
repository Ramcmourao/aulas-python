import os

os.system('cls')

frase = input('Digite uma frase: ').replace(' ', '').lower()

frase_inversa = ''

for c in range(len(frase) - 1, 0 - 1, -1):
    frase_inversa += frase[c]
    
if frase == frase_inversa:
    print('A frase é um palindromo')
else:
    print('A frase não é um palindromo')

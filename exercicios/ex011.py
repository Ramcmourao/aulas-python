'''
Crie um programa que leia uma frase e mostre:
Quantas vezes aparece a letra “a/A”;
Em que posição aparece a primeira vez;
Em que posição aparece a última vez.
'''

frase = input('Digite uma frase: ').strip().upper()

# Quantas vezes aparece a letra A
qtd_a = frase.count('A')
print(f'A letra A aparece {qtd_a} vezes.')

# Em que posição aparece a primeira vez
primeira_pos = frase.find('A')
print(f'A letra A aparece a primeira vez na posição {primeira_pos + 1}.')

# Em que posição aparece a última
ultima_pos = frase.rfind('A')
print(f'A letra A aparece a última vez na posição {ultima_pos + 1}.')

# encontrar a última ocorrência fazendo reverse da frase
frase_inversa = frase[::-1]
ultimo_a = len(frase_inversa) - frase_inversa.find('A')

print(f'A letra A aparece a última vez na posição {ultimo_a}.')
'''
Crie um programa que leia 5 notas de 5 alunos.
Calcule a média, a maior e menor nota.
No final guarde todas as informações organizadas num ficheiro txt.
Crie outro programa que leia o ficheiro.
'''
from pathlib import Path
from statistics import mean
import os

caminho = Path(r'alunos.txt')

with caminho.open('w', encoding='utf-8', errors='ignore') as file:
    
    for c in range(0, 5):
        os.system('cls')
        file.write('----> ')
        nome = input(f'Nome do {c+1} aluno: ')
        file.write(f'{nome}:\n')
        file.write('Notas: ')
        
        notas = list()
        
        for i in range(0, 5):
            nota = float(input(f'Digite a {i+1}ª nota:'))
            file.write(f'{nota:.2f} | ')
            notas.append(nota)
        
        media = mean(notas)
        mais_alta = max(notas)
        mais_baixa =  min(notas)
        
        file.write(f'\nMédia: {media:.2f} | Nota mais alta: {mais_alta:.2f} | Nota mais baixa: {mais_baixa:.2f}\n')

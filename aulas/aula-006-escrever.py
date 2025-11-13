# Para criar/escrever/ler num ficheiro é necessário:
# 1º - Criar uma variável que represente o caminho do ficheiro
# Caminho absoluto - representa todo o percurso desde o disco C: até ao ficheiro
# -> ex: C:\Users\ricar\OneDrive\Formação\Castleform\10805 - Programação em Python\#1\aulas-python\aulas\o-meu-primeiro-codigo.py

# Caminho relativo - representa o percurso desde a pasta do projeto até ao ficheiro
# -> ex: aulas\o-meu-primeiro-codigo.py

from pathlib import Path

FICHEIRO = Path(r'aulas/teste.txt')

# Utilizar o bloco with para abrir o ficheiro, realizar as operações e fechá-lo automagicamente
# Com o bloco with 
# open(modo de abertura, encoding, o que fazer caso haja erros)
# Modo de abertura: 
# -> Read/Leitura - 'r'
# -> Write/Escrita - 'w'
# -> Append/Anexa/Escreve no final - 'a'

with FICHEIRO.open('w', encoding='utf-8', errors='ignore') as file:
    file.write('Olá novamente turma.')
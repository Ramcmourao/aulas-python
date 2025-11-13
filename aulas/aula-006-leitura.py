from pathlib import Path

FICHEIRO = Path(r'aulas\10270.log')

with FICHEIRO.open('r', encoding='utf-8', errors='ignore') as file:
    for linha in file:
        if '[ssl:warn]' in linha.lower():
            print(linha, end='')
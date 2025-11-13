from pathlib import Path

FICHEIRO = Path(r'aulas\10270.log')
SAIDA = r'out.txt'

with FICHEIRO.open('r', encoding='utf-8', errors='ignore') as file:
    
    out = open(SAIDA, 'w', encoding='utf-8', errors='ignore')
    
    for linha in file:
        if 'error' in linha.lower():
            out.write(linha)
            
out.close()
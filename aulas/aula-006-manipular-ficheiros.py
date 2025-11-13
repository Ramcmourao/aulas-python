from pathlib import Path

caminho = Path(r'delfina.txt')

# Escrever Ficheiros
with caminho.open('w', encoding='UTF-8', errors='ignore') as file:
    file.write('A Delfina está atenta!')
    
    
# Ler Ficheiros
with caminho.open('r', encoding='utf-8', errors='ignore') as file:
    for linha in file:
        print(linha)

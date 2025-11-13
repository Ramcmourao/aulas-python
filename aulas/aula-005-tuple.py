# TUPLES SÃO IMUTÁVEIS
# TEMOS DE INICIAR COM VALOREEEEESSSSS

turma = 'Filipe', 'José', 'Eduardo', 'João'

print('for c in range(0, len(turma)):')
for c in range(0, len(turma)):
    print(f'No índice {c} tem {turma[c]}')

print('\nfor nome in turma:')
for nome in turma:
    print(nome)

print('\nfor indice, nome in enumerate(turma):')
for indice, nome in enumerate(turma):
    print(f'No índice {indice} tem {nome}.', flush=True)
    
print('\n\n')
if 'Delfina' in turma:
    print('Delfina está a turma')
else:
    print('Delfina não está na turma.')
    
print('Nomes por ordem alfabética:')

for nome in sorted(turma):
    print(nome)
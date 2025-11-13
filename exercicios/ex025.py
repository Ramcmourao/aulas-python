equipas = ('Real Madrid', 'Barcelona', 'Villarreal',
        'Atlético de Madrid', 'Betis', 'Espanyol', 'Elche', 'Athletic Bilbao', 'Sevilla', 'Alavés', 'Rayo Vallecano', 'Getafe', 'Osasuna', 'Valencia', 'Levante', 'Mallorca', 'Celta', 'Real Oviedo', 'Girona', 'Real Sociedad')

print('-- 5 PRIMEIROS CLASSIFICADOS')
for indice, equipa in enumerate(equipas):
    if indice == 5:
        break
    print(f'\t- {indice+1}º - {equipa}')

print('\n-------------------------------\n')

print('-- 4 ÚLTIMOS CLASSIFICADOS')
TAM = len(equipas)
for indice, equipa in enumerate(equipas):
    if indice >= TAM - 4:
        print(f'\t- {indice+1}º - {equipa}')
    else:
        continue # passa para a próxima iteração
    
print('\n-------------------------------\n')

print('-- EQUIPAS POR ORDEM ALFABÉTICA')
for equipa in sorted(equipas):
    print(f'{equipa}', end=' | ')
    
print('\n-------------------------------\n')

print('-- POSIÇÃO EQUIPA LAS PALMAS')
esta_la = False

for indice, equipa in enumerate(equipas):
    if equipa == 'Las Palmas':
        esta_la = True
        print(f'Las Palmas -> {indice + 1}º lugar.')
        break

if not esta_la:
    print('Equipa Las Palmas não encontrada.')
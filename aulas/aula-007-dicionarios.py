serie = {}
playlist = list()

for c in range(0, 3):
    titulo = input('Digite o titulo: ')
    temporadas = input('Digite o nº de temporadas: ')
    rate = input('Digite a avaliação: ')
    
    serie['Titulo'] = titulo
    serie['Temporada'] = temporadas
    serie['Avaliação'] = rate
    
    playlist.append(serie.copy())

for serie in playlist:
    for chave, valor in serie.items():
        print(f'{chave} -> {valor}')
    print('------------------')
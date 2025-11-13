lista_nomes = ['Delfina', 'Jorge', 'Bruno', 'João']

'''for indice, nome in enumerate(lista_nomes):
    print(f'{indice} -> {nome}')
    
print('Delfina' in lista_nomes)

lista_nomes = list()

for c in range(0, 10):
    nome = input('Digite um nome: ')
    if nome in lista_nomes:
        print('Nome já encontrado na lista')
    else:
        print('Nome adicionado com sucesso')
        lista_nomes.append(nome)'''
        
print(lista_nomes)

lista_nomes.pop(0)

print(lista_nomes)

if 'João Galamba' in lista_nomes:
    lista_nomes.remove('João Galamba')
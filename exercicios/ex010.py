'''
Crie um programa que leia o nome completo de uma pessoa e mostre:
O nome com todas as letras maiúsculas;
O nome com todas as letras minúsculas;
Quantidade de letras sem espaços;
Quantas letras tem o primeiro nome.
'''

nome = input('Digite o seu nome completo: ').strip()

# nome em maiúsculas
print(f'Nome em maiúsculas: {nome.upper()}')

# nome em minúsculas
print(f'Nome em minúsculas: {nome.lower()}')

# Quantidade de letras em espaços
# Com o replace
qtd_letras = len(nome.replace(' ', ''))
print(f'Quantidade de letras sem espaços: {qtd_letras}')

# Com o count dos espaços
qtd_letras = len(nome) - nome.count(' ')
print(f'Quantidade de letras sem espaços: {qtd_letras}')

# Quantas letras tem o primeiro nome
# Com o slit
nome_divido = nome.split()
print(f'O primeiro nome tem {len(nome_divido[0])} caracteres.')

# Com o find
indice_espaco = nome.find(' ')
p_nome = nome[:indice_espaco]
print(f'O primeiro nome tem {len(p_nome)} caracteres.')
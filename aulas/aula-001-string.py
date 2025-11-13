# Concatenação

nome = 'Ricardo'
idade = 33.0
cidade = 'Porto'

print('O nome é:', nome) # concatenação por vírgula (introduz um espaço)
print('O nome é: ' + nome) # concatenação por operador (não introduz espaço)

print('O', nome, 'tem', idade, 'anos e mora no', cidade)
print('O {} tem {} anos e mora no {}'.format(nome, idade, cidade))
print(f'O {nome} tem {idade:.2f} anos e mora no {cidade}')
'''
Crie um programa que leia o primeiro e último nome de uma pessoa e exiba as mensagens:
“Olá nome, o seu registo está completo.”
“O seu email é p.ultimo@empresa.pt”
Ex email: 
Alfredo Xavier
a.xavier@empresa.pt
'''

nome = input('Digite o seu primeiro e último nome: ').strip().lower()
indice_espaco = nome.find(' ')
p_nome = nome[:indice_espaco]
u_nome = nome[indice_espaco+1:]

email = f'{p_nome[0]}.{u_nome}@empresa.pt'

print(f'Olá {p_nome.capitalize()}, o seu registo está completo.')
print(f'O seu email é {email}')
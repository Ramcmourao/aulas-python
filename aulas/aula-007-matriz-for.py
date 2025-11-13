'''alunos = []
dados = list()

for c in range(0, 3):
    nome = input('Digite o seu nome: ')
    media = float(input('Digite a média: '))
    dados.append(nome)
    dados.append(media)
    alunos.append(dados[:])
    dados.clear()
    
print(alunos)
'''

num1 = [1, 2, 3]
num2 = [4, 5, 6]
num3 = [7, 8, 9]

numeros = list()
numeros.append(num1)
numeros.append(num2)
numeros.append(num3)

'''
   0 1 2
0  1 2 3
1  4 5 6
2  7 8 9
'''

for linha in range(0, 3):
    for coluna in range(0, 3):
        print(numeros[linha][coluna], end='')
        
    print()

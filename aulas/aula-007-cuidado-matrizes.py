aluno = list()
aluno.append('Ricardo')
aluno.append(20)
print(aluno)

outro_aluno = list()
outro_aluno.append(aluno)
print(outro_aluno)

aluno[0] = 'Diogo'
aluno[1] = '14'
outro_aluno.append(aluno[:])
print(outro_aluno)

print('Intervalo')
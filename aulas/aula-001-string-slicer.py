import os

os.system('cls')

frase = 'Curso de Python na Castleform'

print(frase[0]) # C
print(frase[9]) # P
print(frase[0:5]) # Curso
print(frase[-1]) # último índice da string
print(frase[9:]) # do índice 9 até ao final
indice_p = frase.find('P') # captura o índice do P
print(frase[indice_p:]) # do índice P até ao final
print(frase.count('P')) # Devolve quantas vezes aparece o P
print(frase.find('Fruta')) # Não encontra e devolve -1
print('curso' in frase) # devolve False pois é case sensitive
print(len(frase)) # devolve o tamanho da String
frase = frase.replace('Python', 'JAVA') # Substitui a palavra antiga pela nova
print(frase) # mostra a frase com a palavra alterada
print(len(frase))# devolve o tamanho da String

print(frase[::-1]) # mostra a frase invertida
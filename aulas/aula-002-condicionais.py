# Limpar o terminal logo no inicio
import os
os.system('cls')

idade = int(input('Digite a sua idade: '))

if idade >= 18:
    print('Pode tirar a carta de condução.')
    
elif idade >= 16:
    print('Pode tirar a carta de condução, mas com autorização.')
    
else:
    print('Não pode tirar a carta.')
    
    print('Fim do programa.')
import os

os.system('cls')

print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
print('-=-=-=- RADAR DE VELOCIDADE -=-=-=-')
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n')

velocidade = int(input('---> '))
LIMITE_VELOCIDADE = 80

if velocidade > LIMITE_VELOCIDADE:
    print('Multado')
    multa = 100 + 7 * (velocidade - LIMITE_VELOCIDADE)
    print(f'MULTA: {multa:.2f}€')

else:
    print('Boa Viagem...')


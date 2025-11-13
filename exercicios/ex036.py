'''
Desenvolva um programa que permita ao utilizador calcular o seu Índice de Massa Corporal (IMC). O programa deve solicitar ao utilizador a sua altura e o seu peso. De seguida, utilizando uma função, deve calcular o IMC e o programa deve exibir uma mensagem com base no valor do IMC calculado.

IMC abaixo de 18,5: Abaixo do peso
IMC entre 18,5 e 24,9: Peso normal
IMC entre 25,0 e 29,9: Sobrepeso
IMC entre 30,0 e 34,9: Obesidade grau 1
IMC entre 35,0 e 39,9: Obesidade grau 2
IMC acima de 40,0: Obesidade grau 3 (obesidade mórbida)
'''

def calcula_imc(altura_metros, peso_kg):
    
    imc = peso_kg / (altura_metros * altura_metros)
    
    if imc < 18.5:
        return f'IMC: {round(imc, 1)} -> Abaixo do peso'
    elif imc < 25:
        return f'IMC: {round(imc, 1)} -> Peso normal'
    elif imc  < 30:
        return f'IMC: {round(imc, 1)} -> Sobrepreso'
    elif imc < 35:
        return f'IMC: {round(imc, 1)} -> Obesidade grau 1'
    elif imc < 40:
        return f'IMC: {round(imc, 1)} -> Obesidade grau 2'
    else:
        return f'IMC: {round(imc, 1)} -> Obesidade grau 3'
        
altura = 0
peso = -1

while altura < 1 or altura > 3: 
    altura = float(input('Digite a altura em metros: '))
    
while peso < 0 or peso > 500:
    peso = float(input('Digite o peso em kg: '))

print(calcula_imc(altura, peso))
'''

Crie um programa que tenha uma função que converta
a temperatura de Celsius para Fahrenheit. 

'''

def conversor(temperatura):
    '''
    -> Converte temperatura de celsius para fahrenheit
    param: temperatura -- é o valor da temperatura em celsius (float)
    return: sem retorno
    '''
    fahrenheit = temperatura * 1.8 + 32
    print(f'{temperatura}ºC -> {fahrenheit}ºF')
    
temp = float(input('Digite a temperatura em Celsius: '))

conversor(temp)
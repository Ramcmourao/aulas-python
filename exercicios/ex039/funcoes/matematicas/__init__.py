from funcoes.utils import cabecalho, ler_int

def tabuada():
    cabecalho('TABUADA')
    
    numero = ler_int('Digite um número: ') # pede um número ao utilizador
    
    # sequencia de prints que mostram a tabuada
    for c in range(0, 10):
            print(f'{numero} x {c+1} = {numero * (c + 1)}')
        
        
def calculadora():
    cabecalho('CALCULADORA')
    expressao = input('Digite a expressão (ex: 2+2)\n--> ') # lê a expressão para calcular
    
    # identifica os índices das operações para poder fatiar a expressão
    indice_mais = expressao.find('+')
    indice_menos = expressao.find('-')
    indice_multiplicar = expressao.find('x')
    indice_dividir = expressao.find('/')
    
    # Caso os índices sejam identificados escolhe qual a operação a ser feita
    # Se o índice tiver o valor -1 significa que não encontrou o operador
    # Caso seja diferente de -1 então é o valor do índice
    if indice_mais != -1:
        num1 = int(expressao[:indice_mais]) # Do índice zero até ao indice do operador é o primeiro número ou numeros
        num2 = int(expressao[indice_mais+1:]) # Do índice do operador +1 é o segundo número ou numeros
        print(num1 + num2)
        
    elif indice_menos != -1:
        num1 = int(expressao[:indice_menos]) # Do índice zero até ao indice do operador é o primeiro número ou numeros
        num2 = int(expressao[indice_menos+1:]) # Do índice do operador +1 é o segundo número ou numeros
        print(num1 - num2)
    
    elif indice_multiplicar != -1:
        num1 = int(expressao[:indice_multiplicar]) # Do índice zero até ao indice do operador é o primeiro número ou numeros
        num2 = int(expressao[indice_multiplicar+1:]) # Do índice do operador +1 é o segundo número ou numeros
        print(num1 * num2)
        
    elif indice_dividir != -1:
        num1 = int(expressao[:indice_dividir]) # Do índice zero até ao indice do operador é o primeiro número ou numeros
        num2 = int(expressao[indice_dividir+1:]) # Do índice do operador +1 é o segundo número ou numeros
        if num2 == 0: # faz uma pequena validação para evitar erros de divisão por zero
            print('ERRO DIVISÃO POR ZERO')
        else:
            print(num1 / num2)
            
            
def numeros_pares():
    cabecalho('NÚMEROS PARES')
    numero = ler_int('Digite um número: ') # pede um numero ao utilizador
    
    if numero % 2 == 0: # se o resto da divisão for zero é PAR
        print(f'O número {numero} é PAR')
    else:
        print(f'O número {numero} é ÍMPAR')
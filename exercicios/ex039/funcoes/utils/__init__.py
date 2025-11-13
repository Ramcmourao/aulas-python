import os
import sys
    
def cabecalho(txt):
    limpa()
    print('-' * 30)
    print(f'{txt:-^30}')
    print('-' * 30)
    
    
def limpa():
    try:
        os.system('cls')
    except:
        pass


def ler_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print('Por favor, digite um número inteiro válido.')
        except KeyboardInterrupt:
            print('Operação cancelado pelo utilizador...')
            sair_programa()


def sair_programa():
    sys.exit()

    
def menu():
    while True:
        cabecalho('CALCULADORA')
        print('[ 1 ] - Tabuada')
        print('[ 2 ] - Calculadora')
        print('[ 3 ] - Números Pares')
        print('[ 4 ] - Sair')
        opcao = ler_int('--> ')
        
        executa_funcoes(opcao)


def executa_funcoes(opcao):
    import funcoes.matematicas
    
    if opcao == 1:
        funcoes.matematicas.tabuada()
    elif opcao == 2:
        funcoes.matematicas.calculadora()
    elif opcao == 3:
        funcoes.matematicas.numeros_pares()
    elif opcao == 4:
        print('A sair...')
        sair_programa()
    else:
        print('Opção inválida...')     
        
    _ = input('--- ENTER para continuar ---')
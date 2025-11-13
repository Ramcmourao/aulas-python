def mostra_menu():
    print('[ 1 ] - Calculadora')
    print('[ 2 ] - Tabuada')
    print('[ 3 ] - Sair')
    opcao = int(input('--> '))
    
    return opcao


def programa(option):
    if option == 1:
        print('Escolheu calculadora')
    elif option == 2:
        print('Escolheu tabuada')
    elif option == 3:
        print('Sair')
    else:
        print('Opção inválida')


def main():
    for c in range(0, 10):
        programa(mostra_menu())


if __name__ == '__main__':
    main()

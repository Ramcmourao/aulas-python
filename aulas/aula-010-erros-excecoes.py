import os

while True:
    os.system('cls')    
    try:
        num1 = int(input('Digite um número: '))
        num2 = int(input('Digite outro número: '))
        
        res = num1 / num2 
        
    except ZeroDivisionError:
        print('Não é possível dividir por zero.')

    except KeyboardInterrupt:
        print('O utilizador preferiu terminar o programa')
        
    except TypeError:
        print('O utilizador não digitou um número inteiro.')
        
    except ValueError:
        print('O utilizador não digitou um número.')
        
    except Exception as e:
        print(f'Ups. Ocorreu um erro: {repr(e)}')
        
    else:
        print(f'{num1} / {num2} = {res}')
        break
        
    finally:
        print('Programa encerrado.')
        _ = input('--- ENTER para continuar ---')

'''
Crie um simulador de crédito habitação simples e sem taxas, que solicite o nome, ano de nascimento, rendimentos mensais, despesas mensais, montante do crédito e prazo em anos, guardando tudo dentro de um dicionário. Calcule, acrescentando ao dicionário, a idade, o remanescente após despesas, quanto deverá pagar mensalmente pelo crédito e se o crédito foi aprovado sempre que o remanescente seja superior ao valor mensal do crédito.

'''

from datetime import datetime

cliente = dict()
ano_atual = datetime.now().year

cliente['nome'] = input('Digite o seu nome: ')
cliente['ano_nascimento'] = int(input('Digite o seu ano de nascimento: '))
cliente['rendimentos_mensais'] = float(input('Digite os seus rendimentos mensais: '))
cliente['despesas_mensais'] = float(input('Digite as suas despesas mensais: '))
cliente['montante_credito'] = float(input('Digite o montante do crédito: '))
cliente['prazo'] = int(input('Digite o prazo em anos: '))
cliente['idade'] = ano_atual - cliente['ano_nascimento']
cliente['remanescente'] = cliente['rendimentos_mensais'] - cliente['despesas_mensais']
cliente['mensalidade'] = cliente['montante_credito'] / (cliente['prazo'] * 12)

# valor se verdade if condição else valor se falso
cliente['situacao'] = 'Aprovado' if cliente['remanescente'] > cliente['mensalidade'] else 'Reprovado'


for k, v in cliente.items():
    print(f'{k} -> {v}')
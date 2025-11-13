class Pessoa:
    def __init__(self, nome, idade, profissao):
        self.nome = nome
        self.idade = idade
        self.profissao = profissao
        
        print(f'Objeto {self.nome} criado com sucesso.')
        
    def mostra_dados(self):
        print(f'{self.nome}, {self.idade}, {self.profissao}')
    
    
    
nova_pessoa = Pessoa('Ricardo', 33, 'Formador')
outra_pessoa = Pessoa('Sara', 21, 'Administrativa')

outra_pessoa.nome

nova_pessoa.mostra_dados()
outra_pessoa.mostra_dados()
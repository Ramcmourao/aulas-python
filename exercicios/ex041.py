'''
Adicione um método à classe desenvolvida no exercício anterior Livro que imprime uma descrição do livro no formato:
“O livro com o titulo X foi escrito pelo autor Y".
'''

class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor


    def mostra(self):
        print(f'O livro {self.titulo} foi escrito pelo autor {self.autor}')


livro1 = Livro('O Principezinho', 'Antoine de Saint-Exupéry')
livro2 = Livro('Atomic Habits', 'James Clear')
livro3 = Livro('Como mentir com estatística', 'Dareell Huff')

livro1.mostra()
livro2.mostra()
livro3.mostra()
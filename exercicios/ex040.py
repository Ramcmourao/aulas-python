'''
Crie uma classe chamada Livro que tenha dois atributos: titulo e autor. Instancie três objeto dessa classe e imprima os valores dos atributos.
'''

class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        

livro1 = Livro('O Principezinho', 'Antoine de Saint-Exupéry')
livro2 = Livro('Atomic Habits', 'James Clear')
livro3 = Livro('Como mentir com estatística', 'Dareell Huff')

print(livro1.titulo)
print(livro1.autor)

print(livro2.titulo)
print(livro2.autor)

print(livro3.titulo)
print(livro3.autor)
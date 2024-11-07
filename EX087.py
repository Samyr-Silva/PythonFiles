## Implemente uma classe chamada “Produto” que possua atributos para armazenar o nome, o preço e a quantidade
## em estoque. Adicione métodos para calcular o valor total em estoque e verificar se o produto está disponível.

from time import sleep
class Produto:

    ## CONSTRUTOR
    def __init__(self, nome, preco, estoque):
        self.nome = nome
        self.preco = preco
        self.estoque = estoque


    ## METODO PARA VER O VALOR TOTAL EM ESTOQUE
    def ValorTotal(self):
        valor = self.preco * self.estoque
        print(f'O valor total do produto "{self.nome}" em estoque é R${valor:.2f}.')


    ## METODO PRA VER O QUANTO DO PRODUTO ESTA EM ESTOQUE
    def Disponivel(self):
        if self.estoque <= 0:
            print(f'O produto "{self.nome}" consta com {self.estoque} EM ESTOQUE.')
        else:
            print(f'O produto "{self.nome}" consta com {self.estoque} EM ESTOQUE.')


## TESTES
prodi = Produto('pasta', 1.25, 0)
prodi.ValorTotal()
prodi.Disponivel()

prodi2 = Produto('água', 3, 9)
prodi2.ValorTotal()
prodi2.Disponivel()
sleep(3)
''' --> Implemente uma classe chamada “Biblioteca” que represente uma
biblioteca virtual. Essa classe deve permitir cadastrar livros,
fazer empréstimos, devolver livros e verificar a disponibilidade de um livro. <-- '''
from menu import leiaInt

## LISTA COM OS LIVROS CADASTRADOS
livros_cadastrados = []
class Biblioteca:
    ##CONSTRUTOR
    def __init__(self, nome_livro):
        self.nome_livro = nome_livro


    ##MÉTODO DE CADASTRAR UM LIVRO
    def CadastrarLivro(self):
        livros = []
        print(f'O livro "\033[1;32m{self.nome_livro}\033[m" foi cadastrado!!')
        livros_cadastrados.append(self.nome_livro)


    ##MÉTODO PRA REQUISITAR UM LIVRO
    def PedirLivro(self):
        if self.nome_livro not in livros_cadastrados:
            print(f'O livro "\033[1;32m{self.nome_livro}\033[m" não temos em nossa biblioteca!')
        else:
            print(f'Foi requisitado o livro "\033[1;32m{self.nome_livro}\033[m"')
            livros_cadastrados.remove(self.nome_livro)


    ##MÉTODO PARA DEVOLVER UM LIVRO
    def DevolverLivro(self):
        if self.nome_livro in livros_cadastrados:
            print(f'O livro "\033[1;32m{self.nome_livro}\033[m" já está na biblioteca!!')
        else:
            print(f'O livro "\033[1;32m{self.nome_livro}\033[m" foi adicionado novamente a biblioteca!!')
            livros_cadastrados.append(self.nome_livro)


##FUNÇÃO PRA MOSTRAR OS LIVROS CADASTRADOS
def MostrarLivros():
    print('-='*20)
    print('LISTA DE LIVROS:'.center(35))
    print('-='*20)
    for c, l in enumerate(livros_cadastrados):
        print(f'\033[36m{c+1}º\033[m -\t\t\033[1;33m{l}\033[m')


##CHECA A DISPONIBILIDADE DE UM LIVRO
def Disponibilidade(nome):
    if nome in livros_cadastrados:
        print(f'Temos o livro "\033[1;32m{nome}\033[m" na biblioteca!!')
    else:
        print(f'Não temos o livro "\033[1;32m{nome}\033[m" na biblioteca!!')
        res = str(input('Quer cadastrar[ S/N ]: ')).strip().upper()[0]
        while res not in 'SN':
            res = str(input('Quer cadastrar[ S/N ]: ')).strip().upper()[0]
        if res == 'S':
            print('O livro foi adicionado a biblioteca!!')
            livros_cadastrados.append(nome)
        else:
            print(f'O livro "\033[1;32m{nome}\033[m" não foi adicionado a bilbioteca!!')

##INTERFACEZINHA
print('-='*30)
print('\033[4;35mBIBLIOTECA VIRTU\033[m'.center(55))
print('-='*30)
while True:
    print('''Seja bem-vindo a biblioteca VIRTU. Escolha o que gostaria de fazer:
    [ 1 ] - Cadastrar Livro:
    [ 2 ] - Requisitar Livro:
    [ 3 ] - Devolver Livro:
    [ 4 ] - Checar Disponibilidade:
    [ 5 ] - Lista Livros: 
    [ 6 ] - Encerrar do Programa:
    ''')

    opc = leiaInt('Sua opção: ')
    while opc > 6 or opc == 0:
        opc = leiaInt('\033[31mOpção inválida.\033[m Sua opção: ')
    ##TESTE LOGICO PARA EXECULTAR A DETERMINADA FUNÇÃO
    if opc == 1:
        livro = Biblioteca(str(input('Nome do livro: ')))
        livro.CadastrarLivro()

    elif opc == 2:
        livro = Biblioteca(str(input('Nome do livro: ')))
        livro.PedirLivro()

    elif opc == 3:
        livro = Biblioteca(str(input('Nome do livro: ')))
        livro.DevolverLivro()

    elif opc == 4:
        Disponibilidade(str(input('Nome do livro: ')))

    elif opc == 5:
        MostrarLivros()

    elif opc == 6:
        break

    pre = str(input('Quer continuar?[ S/N ]: ')).strip().upper()[0]
    while pre not in 'SN':
        pre = str(input('Quer continuar?[ S/N ]: ')).strip().upper()[0]
    if pre == 'N':
        break
##MENSAGEM DE FIM DO PROGRAMA
print('\033[1;31mPROGRAMA "BIBLIOTECA VIRTU" FOI ENCERRADO. VOLTE SEMPRE!!\033[m')
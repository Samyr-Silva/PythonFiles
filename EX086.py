# Implemente uma classe chamada “ContaBancária” que possua atributos para armazenar o
# número da conta, nome do titular e saldo. Adicione métodos para realizar depósitos e saque

##LISTAS PARA FAZER UM TRABALHINHO
nums_conta = []
nomes_conta = []
saldos_conta = []

def LeiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except:
            print("\033[31mERRO. Digite um valor válido: \033[m")
        else:
            return n


class ContaBancaria:

    ## CONSTRUTOR
    def __init__(self, num_conta, nome_titular, saldo):
        self.num_conta = num_conta
        self.nome_titular = nome_titular
        self.saldo = saldo
        nums_conta.append(num_conta)
        nomes_conta.append(nome_titular)
        saldos_conta.append(saldo)


    ## MÉTODO PARA VER INFORMAÇÕES
    def ExibirInfo(self):
        print('-'*30)
        print('DADOS ATUALIZADOS'.center(30))
        print('-'*30)
        print(f'\033[1;33mNúmero da conta:\033[m \t{self.num_conta}')
        print(f'\033[1;33mNome do titular:\033[m \t{self.nome_titular}')
        print(f'\033[1;32mSaldo:\033[m \t\t\t\t{self.saldo}£')


    ## MÉTODO PARA DEPOSITAR, QUANTIA É PASSADA COMO PARAMETRO, E O NÚMERO DA CONTA E MOSTRA OS DADOS ATUALIZADOS
    def Depositar(self, num, quantia=0):
        for i in nums_conta:
            if i == num:
                idx = nums_conta.index(num)
                saldos_conta[idx] += quantia
                Exibir(num)
                print(f'\033[4;32mFoi depositado R${quantia:.2f} na sua conta\033[m')


    ## MÉTODO PARA SACAR, QUANTIA É PASSADA COMO PARAMETRO, E O NÚMERO DA CONTA E MOSTRA OS DADOS ATUALIZADOS
    def Saque(self, num, quantia):
        for i in nums_conta:
            if i == num:
                idx = nums_conta.index(num)
                saldos_conta[idx] -= quantia
                Exibir(num)
                print(f'\033[4;31mFoi sacado R${quantia:.2f} na sua conta\033[m')


## FUNÇÃO PARA EXIBIR OS DADOS FORA DA CLASSE
def Exibir(num_conta, senha=0):
    pose = 0
    for i in nums_conta:
        if i == num_conta:
            print('-' * 30)
            print('DADOS ATUALIZADOS'.center(30))
            print('-' * 30)
            print(f'\033[1;33mNúmero da conta:\033[m \t{nums_conta[pose]}')
            print(f'\033[1;33mNome do titular:\033[m \t{nomes_conta[pose]}')
            print(f'\033[1;32mSaldo:\033[m \t\t\t\t{saldos_conta[pose]}£')
        pose += 1


## INTERFACEZINHA
while True:
    print('''Escolha a opção:
    \033[1;33m[ 1 ] ---- Cadastrar Dados:
    [ 2 ] ---- Exibir Informações:
    [ 3 ] ---- Efetuar Deposito: 
    [ 4 ] ---- Efetuar Saque:
    [ 5 ] ---- Sair do Programa: \033[m''')

    ## OPÇÃO ESCOLHIDA E TESTES LÓGICOS PARA EXECUTAR DETERMINADA FUNCIONALIDADE
    opc = LeiaInt("\033[1;37mDigite a sua opção: \033[m")

    if opc == 1:
        agente = ContaBancaria(int(input("Digite o número da conta: ")), str(input("Nome do titular da conta: ")), float(input("Digite o seu saldo: ")))

    elif opc == 2:
        n = Exibir(int(input("Digite o número da conta: ")))

    elif opc == 3:
        agente.Depositar(int(input("Digite O número da conta: ")), float(input("Valor da quantia: ")))

    elif opc == 4:
        agente.Saque(int(input("Digite o número da conta: ")), float(input("Valor da quantia: ")))

    elif opc == 5:
        break

    else:
        print("\033[31mOPÇÃO INVÁLIDA\033[m")
        opc = LeiaInt("\033[1;37mDigite a sua opção: \033[m")
        while opc > 5 or opc == 0:
            print("\033[31mOPÇÃO INVÁLIDA.\033[m Digite um valor [1/4]")
            opc = LeiaInt("\033[1;37mDigite a sua opção: \033[m")

    cont = str(input("Gostaria de continuar? [S/N] ")).strip().upper()[0]
    while cont not in "SN":
        cont = str(input("Gostaria de continuar? [S/N] ")).strip().upper()[0]
    if cont == "N":
        break


## MENSAGEM DE FIM DO PROGRAMA
print("\033[31mPROGRAMA ENCERRADO. Volte Sempre!!\033[m")

## TALVEZ ADICIONAR O HISTORICO DE DEPOSITOS E SAQUES (AINDA FALTA ISSO)
## TAMBEM VER COMO EU LIMPO O TERMINAL DEPOIS DE FAZER UM ITERAÇÃO
import os

os.system("cls")
# caixa eletronico

def limpa_tela():
    os.system("cls")



def cabecalho():
    print("="*40)
    print("Caixa Eletrônico")
    print("="*40)


def menu():
    print("1 - Consultar Saldo")
    print("2 - Depositar")
    print("3 - Sacar")
    print("4 - Sair")

    print("=" * 40)

def consultar_saldo():
    print(f"\nSaldo Atual: R${saldo:.2f}\n")

def depositar():
    global saldo

    valor = float(input("Valor depositado: R$"))

    if (valor>0):
        saldo += valor
        print("Depósito realizado com sucesso!\n")
        consultar_saldo()
    else:
        print("Valor inválido! Não pode ser negativo ou zero!\n")

def sacar():
    global saldo
    valor = float(input("Valor do saque: R$"))

    if (valor <=0):
        print("Valor inválido! Não pode ser negativo ou zero!\n")
    elif valor>saldo:
        print("Saldo insuficiente para saque\n")
    else:
        saldo -= valor
        print("Saque Realizado!\n")
        consultar_saldo()


#Programa principal
saldo = 1500.00
valor = 0
opcao = 0

while opcao != 4:
    cabecalho()
    menu()

    opcao = int(input("Escolha uma opção: "))

    if(opcao == 1):
        limpa_tela()
        cabecalho()
        consultar_saldo()

    elif (opcao ==2):
        limpa_tela()
        cabecalho()
        depositar()

    elif(opcao==3):
        limpa_tela()
        cabecalho()
        sacar()

    elif(opcao==4):
        print("\nObrigado por utilizar nosso caixa eletrônico!")



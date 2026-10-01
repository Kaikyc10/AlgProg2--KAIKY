saldo = 1000.00
deposito = 1500.00
saque = 2000.00
nome = "Maria"

def deposito(valor, deposito):

    """
    Realiza um depósito na conta.

    Parâmetros:

        valor (float): Saldo atual da conta
        deposito(float): Valor a ser depositado

    Retorno:
        float: Retorna o saldo como positivo
    
    """
    
    if(deposito < 0):
        print("Depósito inválido")

    saldo += valor
    print("Depósito realizado.")
    print(f"Saldo: R${saldo}")

def saque(valor, saque):

    """
    Realiza um saque na conta.

        Parâmetros:
            saldo(float): saldo atual
            valor(float): valor do saque

        Retorno:
            float: novo valor da conta
    
    """
    

    

    if(saque <= valor):
        saldo -= valor
        print("Saque realizado.")
    else:
        print("Meu filho, saldo insuficiente.")

    print(f"Saldo: R$ {saldo}")

def mostra_saldo(nome, valor):

    """
    Exibe o extrato bancário da conta.

    Parâmetros:
        nome(string): nome do cliente
        saldo(float): saldo atual
    
    """

    print("------------------------")
    print(f"Cliente: {nome}")
    print(f"Saldo: R${valor}")
    print("------------------------")


opcao = 0

while opcao != 4:
    print("\n1 - Depositar")
    print("2 - Sacar")
    print("3 - Mostrar Saldo")
    print("4 - Sair")

    opcao= int(input("Escolha a opção: "))

    if(opcao ==1):
        deposito(saldo, deposito)
    elif(opcao ==2):
        saque(saldo,saque)
    elif(opcao == 3):
        mostra_saldo(nome, saldo)
    elif(opcao == 4):
        print("Programa encerrado.")
    else:
        print("Número errado Ô kbaço")

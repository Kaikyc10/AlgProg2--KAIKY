import os

os.system("cls")

def cabecalho():
    print("="*40)
    print("SISTEMA DE CADASTRO")
    print("="*40)

def menu():
    print("1 - Cadastrar Dados")
    print("2 - Consultar RA")
    print("3 - Relatório")
    print("4 - Sair")
    print("=" * 40)

def limpa_tela():
    os.system("cls")


def cadastrar():
    ra = int(input("Bem vindo! Digite seu RA:"))
    nome = input("Digite seu nome: ")
    email = input("digite seu email: ")


import os
import re

os.system("cls")

alunos = []

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



def validar_ra(ra):
    
    ra_str = str(ra)
    
    while len(ra_str) !=9:
        ra = int(input("RA inválido, digite novamente:"))
        ra_str = str(ra)

    return ra

        


def validar_email(email):
    

    email_minusculo = email.lower().strip()
    posicao_arroba = email_minusculo.find("@")
    posicao_ponto_com = email_minusculo.find(".com")

    while posicao_arroba == -1 or posicao_ponto_com == -1:
        email = input("Email inválido, digite novamente:")

        email_minusculo = email.lower().strip()
        posicao_arroba = email_minusculo.find("@")
        posicao_ponto_com = email_minusculo.find(".com")

    return email






def cadastrar():
    ra = int(input("Bem vindo! Digite seu RA:"))
    ra = validar_ra(ra)
    nome = input("Digite seu nome:")
    email = input("digite seu email:")
    email = validar_email(email)

    alunos.append([ra,nome,email])

    print("Cadastro realizado!")




def consultar():
    ra = int(input("Digite o RA cadastrado:"))

    for aluno in alunos:
        if aluno[0] == ra:
            print(f"RA: {aluno[0]}")
            print(f"Aluno: {aluno[1]}")
            print(f"Email: {aluno[2]}")
            print("="*20)
            return

    print("Aluno não cadastrado.")



def exibir_relatorio():
    for aluno in alunos:

        ra = aluno[0]
        nome = aluno[1]
        email = aluno[2]

        
        print(f"RA: {ra}")
        print(f"Aluno: {nome}")
        print(f"Email: {email}")
        print("="*20)



opcao = 0

while opcao != 4:
    cabecalho()
    menu()

    opcao = int(input("Escolha uma opção:"))

    if(opcao==1):
        limpa_tela()
        cabecalho()
        cadastrar()
    elif(opcao==2):
        limpa_tela()
        cabecalho()
        consultar()
    elif(opcao==3):
        limpa_tela()
        cabecalho()
        exibir_relatorio()



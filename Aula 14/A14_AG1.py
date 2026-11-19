def registrar_log(tipo, mensagem):
    with open("sistema.log", "a") as arquivo:
        arquivo.write(f"[{tipo}] {mensagem}\n")


def cadastrar_aluno():
    print("\n-- Cadastro de Aluno --")

    ra = int(input("RA: "))
    nome = input("Nome: ")
    nota = float(input("Nota: "))

    with open("alunos.txt", "a") as arquivo:
        arquivo.write(f"{ra}; {nome}; {nota}\n")
    
    registrar_log("CADASTRO", f"RA {ra} cadastrado")


def listar_alunos():
    print("\n--- Alunos Cadastrados ---")


    with open("alunos.txt") as arquivo:
        for linha in arquivo:
            dados = linha.strip().split(";")
            ra = int(dados[0])
            nome = dados[1]
            nota = float(dados[2])

            print(f"RA: {ra} | Nome: {nome} | Nota: {nota:.1f}")
        
    registrar_log("LISTAGEM", "Listagem de alunos realizada")


def pesquisar_aluno():
    print("\n --- Pesquisar Aluno ---")

    ra_busca = int(input("Digite o RA: "))
    encontrado = False

    with open("alunos.txt","r") as arquivo:
        for linha in arquivo:
            dados = linha.strip().split(';')

            ra = int(dados[0])
            nome = dados[1]
            nota = float(dados[2])

            if( ra == ra_busca):
                encontrado = True

                print("\nAluno encontrado!")
                print(f"RA: {ra}")
                print(f"Nome: {nome}")
                print(f"Nota: {nota:.1f}")
                break

        if (encontrado):
            registrar_log("BUSCA", f"RA {ra_busca} encontrado")
        else:
            print("Aluno não encontrado!")
            registrar_log("BUSCA", f"RA {ra_busca} não encontrado")


def alterar_nota():
    print("\n---Alterar Nota---")

    ra_busca = int(input("Digite o RA: "))
    alunos = []
    nota_alterada = False

    with open ("alunos.txt","r") as arquivo:
        for linha in arquivo:
            dados = linha.strip().split(";")
            ra = int(dados[0])
            nome = dados [1]
            nota = float(dados[2])

            

            if(ra == ra_busca):
                nota_alterada: True
                print(f"\nAluno {nome}")
                print(f"Nota Atual: {nota}")

                nova_nota = float(input("Digite a nova nota: "))
                if(nova_nota != nota):
                    nota_alterada = True
                    nota = nova_nota

            aluno = [ra,nome,nota]
            alunos.append(aluno)

    if (nota_alterada):
        with open("alunos.txt", "w") as arquivo:
            for aluno in alunos:
                arquivo.write(f"{aluno[0]}; {aluno[1]}; {aluno[2]}\n")

        registrar_log("ALTERACAO", f"RA {ra_busca} teve a nota alterada")
    else:
        print(f"RA {ra_busca} não teve alteração")
        registrar_log("ALTERACAO", f"RA {ra_busca} tentativa de alteracao")



registrar_log("INFO", "Sistema iniciado")



while True:
    print("\n======Sistema de Aulas======")
    print("\n1- Cadastrar Aluno")
    print("\n2- Alterar Nota de Aluno")
    print("\n3 - Listar Alunos")
    print("\n4 - Pesquisar Aluno")
    print("\n5 - Sair")

    opcao = input("\nEscolha uma opção: ")

    if(opcao == "1"):
        cadastrar_aluno()
    elif(opcao == "2"):
        alterar_nota()
    elif(opcao == "3"):
        listar_alunos()
    elif(opcao=="4"):
        pesquisar_aluno()
    elif (opcao=="5"):
        print("Encerrando programa...")
        break
    else:
        print("Opção inválida")
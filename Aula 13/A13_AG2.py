from pathlib import Path

pasta_do_py = Path(__file__).parent
print(pasta_do_py)
nome_do_arquivo = pasta_do_py/"alunos.txt"

def ler_arquivo(arquivo):
    with open (arquivo, "r") as arquivo:
        alunos = arquivo.readlines()

        for aluno in alunos:
            print(aluno.strip())

            

ler_arquivo(nome_do_arquivo)




with open (nome_do_arquivo, "a") as arquivo:
    arquivo.write("Bonnie")





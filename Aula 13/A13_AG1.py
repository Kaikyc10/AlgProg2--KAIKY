from pathlib import Path
pasta_do_py = Path(__file__).parent
nome_do_arquivo = pasta_do_py/"alunos.txt"


arquivo = open(nome_do_arquivo, "r")

print("=========Leitura 1")
conteudo = arquivo.read()

print(conteudo)

arquivo.close()

arquivo = open(nome_do_arquivo, "r")
print("Lendo a linha 1==========")
linha1 = arquivo.readline()
print(linha1)

arquivo.close()

print("usando um laço")

arquivo = open(nome_do_arquivo, "r")
for linha in arquivo:
    print("lendo a linha========>")
    print(linha)
arquivo.close()
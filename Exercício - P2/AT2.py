ARQUIVO_TESTE = "teste.txt"

def registrar_teste(teste,texto):
    with open(ARQUIVO_TESTE,"a") as arquivo:
        linha = f"teste {teste} - {texto}\n"
        arquivo.write(linha)

    print(linha)

registrar_teste(1,"Bonnie")
registrar_teste(2, "Pequena")
registrar_teste(3, "Popó")
registrar_teste(4, "Pretinho")
registrar_teste(5, "Pigão")
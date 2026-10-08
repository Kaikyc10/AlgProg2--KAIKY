def pessoa(nome, idade, cidade):
    print(f"Nome: {nome}, idade {idade} e cidade {cidade}")

pessoa("Billy", 30, "Americana")

def pessoa2(**dados):
    for chave, valor in dados.items():
        print(f"{chave}: {valor}")


dadosPessoa = {
    "nome" : "Billy",
    "cidade" : "Americana",
    "idade" : 20
}

pessoa2(**dadosPessoa)


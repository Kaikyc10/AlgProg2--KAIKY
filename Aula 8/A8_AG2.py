def cadastrar(nome,idade,cidade):
    print(f"Nome: {nome}")
    print(f"Idade: {idade}")
    print(f"Cidade: {cidade}")

print("==== Posicional ====")
cadastrar("João",18,"Curitiba")
print("========================")
cadastrar("Maria",30,"SP")

print("\n==== Nomeado ====")
cadastrar(nome="Pedrinho", idade=30, cidade="Campinas")
print("====================================")
cadastrar(nome="Bonnie", cidade="Cosmópolis", idade=12)
print("====================================")
cadastrar("Emilio", cidade="RJ", idade=42)
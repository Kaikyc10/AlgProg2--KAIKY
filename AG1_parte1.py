import os
os.system('cls')


#Aula 4 - Manipulação de strings

print("=" * 50)
print("Cadasto de Usuário")
print("=" * 50)

nome = input("Nome completo: ").strip()
nome = nome.title()

email = input("E-mail: ").strip().lower()

senha = input("Senha: ")

nome_valido = len(nome)>0
email_valido =(
    "@" in email and 
    "." in email and
    email.find("@")>0
)

tem_numero = False

for caracter in senha:
    if caracter.isdigit():
        tem_numero = True
senha_valida = len(senha) >= 8 and tem_numero

#Resultado

print("\nResultado\n")
print(f"Nome: {nome}")
print(f"E-mail: {email}")
print()

if nome_valido:
    print("🧅 Nome Válido")
else:
    print("🌭Nome Inválido")

if email_valido:
    print("🧅 E-mail Válido")
else:
    print("🌭E-mail Inválido")

if senha_valida:
    print("🧅 Senha Válida")
else:
    print("🌭Senha Inválida")

if nome_valido and email_valido and senha_valida:
    print("\nCadastro realizado com sucesso!")
else:
    print("Faz sapoha dnv")

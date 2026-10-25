from tokenize import Double


def media(*notas):
    media = sum(notas)/len(notas)
    print(f"A média é: {media}")

n1 = float(input("Digite a 1ª nota: "))
n2 = float(input("Digite a 2ª nota: "))
n3 = float(input("Digite a 3ª nota: "))

media(n1,n2,n3)


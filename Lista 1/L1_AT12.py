def somatorio (numero):
    somatorio = 1

    for i in range (2,numero+1,1):
        somatorio = somatorio + i
        

    print(f"O somatório total é: {somatorio}")


n = int(input("Digite o valor para somatório: "))

somatorio(n)
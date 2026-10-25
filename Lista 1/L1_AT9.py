def verificar_triangulo(a,b,c):
    if ((a>=b+c) or (b>=a+c) or (c>=a+b)):
        print("Não formam um triângulo")
    else:
        if ((a==b) and (b==c)):
            print("Triângulo Equilátero")
        else:
            if ((a==b) or (b==c) or (a==c)):
                print("Triângulo Isóceles")
            else:
                if((a!=b) and (b!=c) and (a!=c)):
                    print("Triângulo Escaleno")

a = float(input("Informe o 1º valor: "))
b = float(input("Informe o 2º valor: "))
c = float(input("Informe o 3º valor: "))

verificar_triangulo(a,b,c)
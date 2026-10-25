import math

def imc(peso,altura):
    imc = peso/math.pow(altura,2)

    if (imc <18.5):
        print("Peso abaixo do ideal")
    else:
        if(imc>=18.5 and imc<25):
            print("Peso normal")
        else:
            if(imc >=25 and imc<30):
                print("Sobrepeso")
            else:
                if(imc >=30 and imc<35):
                    print("Obesidade Grau I")
                else:
                    if(imc >=35 and imc<40):
                        print("Obesidade Grau II")
                    else:
                        if(imc>=40):
                            print("Obesidade Grau III")

p = float(input("Digite seu peso (kg): "))
a = float(input("Digite sua altura(m): "))

imc(p,a)
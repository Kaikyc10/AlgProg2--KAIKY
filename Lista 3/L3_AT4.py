def calcular_area_trapezio(base_menor, base_maior, altura):
    return (base_menor + base_maior) * altura / 2

def main():
    base_menor = float(input("Digite o comprimento da base menor do trapézio: "))
    base_maior = float(input("Digite o comprimento da base maior do trapézio: "))
    altura = float(input("Digite a altura do trapézio: "))

    print(f"Área do trapézio: {calcular_area_trapezio(base_menor, base_maior, altura)}")

main()
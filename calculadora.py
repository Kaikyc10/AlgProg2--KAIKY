from datetime import datetime
import math
import matplotlib.pyplot as plt

ARQUIVO_HISTORICO = "historico_estatistico.txt"


def registrar_historico(operacao, resultado):
    agora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    linha = f"[{agora}] {operacao} -> Resultado: {resultado}\n"
    with open(ARQUIVO_HISTORICO, "a", encoding="utf-8") as arquivo:
        arquivo.write(linha)


def ver_historico():
    print("\n===== HISTÓRICO DE OPERAÇÕES =====")
    try:
        with open(ARQUIVO_HISTORICO, "r", encoding="utf-8") as arquivo:
            conteudo = arquivo.read().strip()
            if not conteudo:
                print("O histórico ainda está vazio.")
            else:
                print(conteudo)
    except FileNotFoundError:
        print("Nenhum histórico encontrado ainda. Realize uma operação primeiro.")
    print("===================================")


def media(numeros):
    if not numeros:
        return 0
    return sum(numeros) / len(numeros)


def moda(numeros):
    if not numeros:
        return 0

    numeros_organizados = sorted(numeros)
    moda_atual = numeros_organizados[0]
    frequencia_max = 1

    numero_atual = numeros_organizados[0]
    frequencia_atual = 1

    for i in range(1, len(numeros_organizados), 1):
        if numeros_organizados[i] == numero_atual:
            frequencia_atual = frequencia_atual + 1
        else:
            numero_atual = numeros_organizados[i]
            frequencia_atual = 1

        if frequencia_atual > frequencia_max:
            frequencia_max = frequencia_atual
            moda_atual = numero_atual

    if frequencia_max <= 1:
        return 0

    return moda_atual


def mediana(numeros):
    if not numeros:
        return 0

    numeros_organizados = sorted(numeros)
    n = len(numeros_organizados)
    meio = n // 2

    if n % 2 == 0:
        return (numeros_organizados[meio - 1] + numeros_organizados[meio]) / 2
    else:
        return numeros_organizados[meio]


def q1(numeros):
    if not numeros:
        return 0

    numeros_organizados = sorted(numeros)
    n = len(numeros_organizados)
    pos = (n + 1) / 4

    inteiro = int(pos)
    decimal = pos - inteiro

    if decimal == 0:
        return numeros_organizados[inteiro - 1]
    else:
        valor_inferior = numeros_organizados[inteiro - 1]
        valor_superior = numeros_organizados[inteiro]
        return valor_inferior + decimal * (valor_superior - valor_inferior)


def q3(numeros):
    if not numeros:
        return 0

    numeros_organizados = sorted(numeros)
    n = len(numeros_organizados)
    pos = 3 * (n + 1) / 4

    inteiro = int(pos)
    decimal = pos - inteiro

    if decimal == 0:
        return numeros_organizados[inteiro - 1]
    else:
        valor_inferior = numeros_organizados[inteiro - 1]
        valor_superior = numeros_organizados[inteiro]
        return valor_inferior + decimal * (valor_superior - valor_inferior)


def percentil(p_desejado, numeros):
    if not numeros:
        return 0

    numeros_organizados = sorted(numeros)

    if p_desejado < 1:
        return numeros_organizados[0]
    if p_desejado >= 100:
        return numeros_organizados[-1]

    p = (p_desejado * (len(numeros_organizados) + 1)) / 100
    return numeros_organizados[int(p) - 1]


def variancia(numeros):
    if not numeros:
        return 0

    soma = 0
    for i in range(0, len(numeros), 1):
        soma = soma + numeros[i]

    media_calc = soma / len(numeros)

    somatorio = 0
    for j in range(0, len(numeros), 1):
        somatorio = somatorio + ((numeros[j] - media_calc) ** 2)

    return somatorio / len(numeros)


def desvio_padrao(var):
    return math.sqrt(var)


def coeficiente_v(desvio, med):
    return (desvio / med) * 100


def histograma(numeros):
    if not numeros:
        print("Insira números primeiro")
        return False

    plt.hist(numeros, bins="auto", edgecolor="black")
    plt.title("Histograma dos Valores")
    plt.xlabel("Valores")
    plt.ylabel("Frequência")
    plt.grid(axis="y", alpha=0.3)
    plt.show()
    return True


# --- EXECUÇÃO DO PROGRAMA ---

print("===== CALCULADORA ESTATÍSTICA =====")
print("Bem-vindo(a) à Calculadora Estatística!\n")

qtde = int(input("Para começarmos, quantos valores você deseja inserir? : "))
numeros = []

print(f"Certo, vamos trabalhar com {qtde} números!")

for i in range(qtde):
    val = float(input(f"Digite o valor nº{i+1}: "))
    numeros.append(val)

print("\nNúmeros registrados!")
print(numeros)
print()

continuar = True
opcoes_validas = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

while continuar:
    print("===== OPERAÇÕES ESTATÍSTICAS =====")
    print("1 - Moda")
    print("2 - Média")
    print("3 - Mediana")
    print("4 - Quartis")
    print("5 - Percentis")
    print("6 - Variância")
    print("7 - Desvio-Padrão")
    print("8 - Sair")
    print("9 - Gerar Histograma")
    print("10 - Ver Histórico")
    print("====================================")

    opcao = int(input("Digite a operação desejada: "))

    while opcao not in opcoes_validas:
        opcao = int(input("Opção inválida, digite novamente: "))

    if opcao == 1:
        resultado = moda(numeros)
        print("A Moda é:", resultado)
        registrar_historico(f"Moda de {numeros}", resultado)

    elif opcao == 2:
        resultado = media(numeros)
        print("A Média é:", resultado)
        registrar_historico(f"Média de {numeros}", resultado)

    elif opcao == 3:
        resultado = mediana(numeros)
        print("A mediana é:", resultado)
        registrar_historico(f"Mediana de {numeros}", resultado)

    elif opcao == 4:
        q = int(input("Digite 1 p/Q1 ou 3 p/Q3: "))
        while q != 1 and q != 3:
            print("Número inválido, digite novamente.")
            q = int(input("Digite 1 p/Q1 ou 3 p/Q3: "))

        if q == 1:
            resultado = q1(numeros)
            print("O valor de Q1 é:", resultado)
            registrar_historico(f"Q1 de {numeros}", resultado)
        else:
            resultado = q3(numeros)
            print("O valor de Q3 é:", resultado)
            registrar_historico(f"Q3 de {numeros}", resultado)

    elif opcao == 5:
        p = int(input("Qual o percentil desejado? : "))
        while p < 0 or p > 100:
            p = int(input("Valor inválido. Digite novamente: "))
        resultado = percentil(p, numeros)
        print("O valor é:", resultado)
        registrar_historico(f"Percentil {p} de {numeros}", resultado)

    elif opcao == 6:
        resultado = variancia(numeros)
        print("A Variância é:", resultado)
        registrar_historico(f"Variância de {numeros}", resultado)

    elif opcao == 7:
        v = variancia(numeros)
        resultado = desvio_padrao(v)
        print("O Desvio-Padrão é:", resultado)
        registrar_historico(f"Desvio-Padrão de {numeros}", resultado)

    elif opcao == 9:
        if histograma(numeros):
            registrar_historico(f"Histograma de {numeros}", "Gráfico exibido")

    elif opcao == 10:
        ver_historico()

    elif opcao == 8:
        print("\n================================================")
        print("Obrigado por usar a Calculadora Estatística!")
        print("================================================")
        print("Este projeto foi feito por:\n")
        print("Lucas Palestino - 202610049")
        print("Kaiky Tereza - 202610079")
        continuar = False

    print()
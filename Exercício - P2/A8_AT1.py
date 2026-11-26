def analisar_turma(*notas,media_minima=6.0,**dados):

    media = sum(notas)/len(notas)


    maior = 0
    menor = 11

    aprovados = 0
    reprovados = 0

    

    for i in range(0,len(notas),1):
        if(notas[i] > maior):
            maior = notas[i]
        if(notas[i] < menor):
            menor = notas[i]
        if(notas[i] > media_minima):
            aprovados = aprovados + 1
        if(notas[i] < media_minima):
            reprovados = reprovados + 1


    percent_aprovacao = (aprovados/len(notas))*100

    print(f"Média: {media}")
    print(f"Quantidade de aprovados: {aprovados}")
    print(f"Quantidade de reprovados: {reprovados}")
    print(f"Percentual de aprovação: {percent_aprovacao}%")
    print(f"Maior nota: {maior}")
    print(f"Menor nota: {menor}")



    for chave, valor in dados.items():
        print(f"{chave}: {valor}")


analisar_turma(10,5,9.5,4.3, media_minima=7.0, curso="Computação",professor="Careca fdp", melhor="Kaiky")








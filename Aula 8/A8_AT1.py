def analisar_turma(*notas, media_minima=6.0, **dados):

    """
    Analisa todos os dados fornecidos a respeito da turma.

    A função recebe como parâmetro:

    - *notas: quantidade indefinida de notas dos alunos. O parâmetro é do tipo *args;

    - media_minima: Valor da média mínima para o aluno ser aprovado. O parâmetro é do tipo
    double e recebe como valor padrão 6.0;

    - **dados: Informações adicionais sobre a turma. O parâmetro é do tipo **kwargs.

    """

    soma = sum(notas)
    media = soma/len(notas)

    maior = -1
    menor = 11
    reprovados = 0
    aprovados = 0


    for i in range(0,len(notas),1): 
        if (notas[i] > maior):
            maior = notas[i]
        if(notas[i]<menor):
            menor = notas[i]
        if(notas[i]<media_minima):
            reprovados = reprovados + 1
        if(notas[i] >= media_minima):
            aprovados = aprovados + 1

    percentual_aprovacao = (aprovados*100)/len(notas)

    print("---Dados da Turma---")
    for chave,valor in dados.items():
        print(f"{chave}:{valor}")
        

    return {
        "media": media,
        "maior": maior,
        "menor": menor,
        "aprovados": aprovados,
        "reprovados": reprovados,
        "percentual": percentual_aprovacao
    }

resultado = analisar_turma(7.5,6,9.5,10,9.8,5.5,4,3,6,10,
                           media_minima=6.0,
                           disciplina="Programação",
                           professor="Billy",
                           turma = "1")

print(resultado)
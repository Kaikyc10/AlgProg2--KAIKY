def cadastrar_evento(nome, *participantes,  online=False, **informacoes):

    """
    A função cadastra um evento conforme os dados fornecidos pelo usuário.

    Recebe como parâmetros:

    - nome: Variável que leva o nome do evento fornecido pelo usuário;
    - *participantes: Quantidade indefinida de participantes. Esse parâmetro é do tipo *args;
    - online=False: Do tipo boolean, recebe o status do evento e leva como valor padrão True;
    - **informacoes: Informações adicionais do evento. O parâmetro é do tipo **kwargs.
    
    """

    total = len(participantes)

    info_ordenada = sorted(informacoes.items())

    print("=====DADOS DO EVENTO====")

    print(f"EVENTO - {nome}")

    for i in range(0, len(participantes),1):
        print(f"Participante {i+1} - {participantes[i]}")
    print("============================")
    
    for chave,valor in info_ordenada:
        print(f"{chave}:{valor}")

    print("==========================")

    print(f"Total de participantes: {total}")


cadastrar_evento("Comic-Con",
                 "Tom Cruise",
                 "Sir Ian Mckelen",
                 "Christopher Nolan",
                 "Selton Mello",
                 filme="Thundercats",
                 produtora="Artbac Studios",
                 classificacao="14 anos",
                 data="15/09/2027")


def criar_perfil(**dados):

    """
    A função cria um perfil conforme os dados fornecidos pelo usuário.

    recebe como parâmetro:

    - **dados: São os dados que o usuário irá informar. O parâmetro é do tipo **kwargs.
    
    """

    if not dados:
            print("Nenhum dado registrado!")
            return

    print("=====DADOS DO PERFIL=====")

    dados_ordenados = sorted(dados.items())


    for chave,valor in dados_ordenados:
        print(f"{chave}:{valor}")

    print("==================================")

    print(f"Total de atributos: {len(dados)}")

criar_perfil(filme="Projeto Dejavú",
             diretor="Kaiky Tereza",
             formato="IMAX",
             ano_lancamento="2032")
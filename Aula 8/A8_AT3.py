def criar_perfil(**dados):

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
def liha_do_tempo(*eventos):
    total = len(eventos)

    if not eventos:
        print("Nenhum evento registrado!")
        return

    print("=====LINHA DO TEMPO=====")

    eventos_ordenados = sorted(eventos)

    for ano,descricao in eventos_ordenados:
        print(f"{ano} - {descricao}")

    print("==============================")

    print(f"Total de eventos: {total}")


liha_do_tempo(
    (1987, "Comi picanha metafísica"),
    (1990, "Fiz um gol de bike"),
    (1405, "Nascimento Edson Arantes do Nascimento Sr.")
)
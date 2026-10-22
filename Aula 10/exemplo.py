def contagem(n):

    print(n)

    if n == 0:
        return

    contagem(n - 1)


contagem(5)
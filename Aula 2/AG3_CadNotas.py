#Cadastro de notas utilizando matriz

#Lista para armazenar todos os alunos
alunos = []

#quantidade de alunos

quantidade = 3

#leitura nos dados
for i in range (quantidade):
    print(f"\nAluno {i+1}")
    nome = input("Nome: ")

    notas = []

    for j in range(3):
        nota = float(input(f"Nota {j+1}:"))
        notas.append(nota)

    alunos.append([nome,notas])

    print("\nRelatório\n")

    for aluno in alunos:
        nome = aluno[0]
        notas = aluno[1]
        media = sum(notas)/len(notas)
        print(f"Média: {media:.2f}")

        if media >=6:
            print("Situação: APROVADO")
        else:
            print("Situação: KKKKKKKKKKK")
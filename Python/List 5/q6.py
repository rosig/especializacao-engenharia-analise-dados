alunos = []

for index in range(3):
    alunos.append(
        [
            input(f"Nome do aluno {index}: "),
            float(input("Primeira nota: ")),
            float(input("Segunda nota: ")),
            float(input("Terceira nota nota: ")),
        ]
    )

for aluno in alunos:
    media = sum(aluno[1:]) / 3
    print(
        f"A média de {aluno[0].capitalize()} é {media:.2f} e ele(a) está {'reprovado(a)' if media < 7 else 'aprovado(a)'}."
    )

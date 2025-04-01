notas_estudantes = []

for numero_estudante in range(5):
    primeira_nota = float(
        input(f"Escreva a primeira nota do aluno {numero_estudante}: ")
    )
    segunda_nota = float(input(f"Escreva a segunda nota do aluno {numero_estudante}: "))
    notas_estudantes.append([primeira_nota, segunda_nota])

medias_notas = [(sum(notas) / len(notas)) for notas in notas_estudantes]

print(f"Médias: {medias_notas}")
print(
    f"Número de estudantes com média >= 7: {len([media for media in medias_notas if media >= 7])}"
)

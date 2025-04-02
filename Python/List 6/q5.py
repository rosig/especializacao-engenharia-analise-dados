NUMERO_CORREDORES = 4

dict_corredores = {}  # {nome: [tempos]}

for num in range(NUMERO_CORREDORES):
    dict_corredores.update(
        {
            input(f"Nome do corredor {num}: "): [
                float(input("Tempo 1: ")),
                float(input("Tempo 2: ")),
                float(input("Tempo 3: ")),
            ]
        }
    )

campeao = ("", float("inf"))

for nome, tempos in dict_corredores.items():
    media = sum(tempos) / len(tempos)
    if media < campeao[1]:
        campeao = (nome, media)

print(
    f"O campeão é {campeao[0].upper()} com média de tempo de {campeao[1]:.2f} segundos."
)

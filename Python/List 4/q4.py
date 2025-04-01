meses = [
    "Janeiro",
    "Fevereiro",
    "Março",
    "Abril",
    "Maio",
    "Junho",
    "Julho",
    "Agosto",
    "Setembro",
    "Outubro",
    "Novembro",
    "Dezembro",
]

media = 0
temperatura = 0

for index in range(len(meses)):
    temperatura = int(input(f"Temperatura de {meses[index]}: "))
    meses[index] = (meses[index], temperatura)
    media += temperatura

    if index == 11:
        media = media / 12

print(f"Média Anual de Temperaturas: {media}")
print("Meses com temperaturas acima da média:")

for nome_mes, temperatura_mes in meses:
    if temperatura_mes > media:
        print(nome_mes)

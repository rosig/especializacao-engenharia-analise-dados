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

data_nascimento = input("Data de nascimento: ")

dia, mes, ano = data_nascimento.split("/")

print(f"Você nasceu em {dia} de {meses[int(mes)-1]} de {ano}")

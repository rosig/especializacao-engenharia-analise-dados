suites = {
    1: {"nome": "Suíte Standard", "valor_noite": 250, "limite_noites": 15},
    2: {"nome": "Suíte Luxo", "valor_noite": 500, "limite_noites": 10},
    3: {"nome": "Suíte Presidencial", "valor_noite": 1200, "limite_noites": 7},
}

print(
    f"""
=== Tipos de Suíte ==
      1 - Standard
      2 - Luxo
      3 - Presidencial
"""
)


def calcula_preco(quantidade_noites, valor_noite):
    percentual_desconto = 0

    if quantidade_noites >= 5:
        percentual_desconto = 10

    return (quantidade_noites * valor_noite) * (1 - (percentual_desconto / 100))


tipo_suite = int(input("Escolha o da suíte que deseja: "))
quantidade_noites = int(input("Informe a quantidade de noites que deseja ficar: "))
suite_selecionada = suites.get(tipo_suite, None)

if suite_selecionada:
    nome_suite = suite_selecionada["nome"]
    limite_noites = suite_selecionada["limite_noites"]
    valor_noite = suite_selecionada["valor_noite"]

    if quantidade_noites <= limite_noites:
        print(
            f"Valor total da estadia: R$ {calcula_preco(quantidade_noites, valor_noite)} "
        )
    else:
        print(
            f"""
          O limite de noites foi atingido.
          Você pode ficar no máximo {limite_noites} noites na {nome_suite}.
          Caso queira ficar por {limite_noites} noites, o valor total da estadia será de R$ {calcula_preco(limite_noites, valor_noite)}
              """
        )
else:
    print("Número inválido!")

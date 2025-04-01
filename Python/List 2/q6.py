def calcula_preco(preco_sessao, idade_pessoa):
    percentual_desconto = 0

    if idade_pessoa <= 12 or idade_pessoa >= 65:
        percentual_desconto = 50
    else:
        carteira_estudante = input(
            f"""
              Você tem carteira de estudante?
                - Escreva S de Sim
                - Escreva N de Não
              """
        )

        if carteira_estudante == "S":
            percentual_desconto = 50

    return preco_sessao * (1 - (percentual_desconto / 100))


dict_sessoes = {
    1: {"nome": "Matinê", "preco": 20},
    2: {"nome": "Vespertina", "preco": 25},
    3: {"nome": "Noturna", "preco": 30},
}

print(
    f"""
=== Tipos de Sessão ==
      1 - Matinê
      2 - Vespertina
      3 - Noturna
"""
)

tipo_sessao = int(input("Escolha o número do tipo de sessão que deseja: "))
sessao_selecionada = dict_sessoes.get(tipo_sessao, None)

if sessao_selecionada:
    idade = abs(int(input("Informe sua idade: ")))
    valor_ingresso = calcula_preco(sessao_selecionada["preco"], idade)
    print(f"Valor do ingresso: R$ {valor_ingresso}")
else:
    print("Número de sessão inválido!")

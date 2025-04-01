dict_planos = {
    "basico": {
        "limite_minutos_telefonia": 100,
        "limite_internet_gigas": 5,
        "preco": 50,
    },
    "intermediario": {
        "limite_minutos_telefonia": 300,
        "limite_internet_gigas": 10,
        "preco": 80,
    },
    "avancado": {
        "limite_minutos_telefonia": 500,
        "limite_internet_gigas": 20,
        "preco": 120,
    },
}


def calcula_preco(plano, minutos_telefonia_utilizados, gigas_utilizados):
    plano_selecionado = dict_planos.get(plano, None)

    if plano_selecionado:
        valor_final = plano_selecionado["preco"]

        minutos_excedentes = (
            minutos_telefonia_utilizados - plano_selecionado["limite_minutos_telefonia"]
        )

        while minutos_excedentes > 0:
            valor_final += 1
            minutos_excedentes -= 1

        gigas_excedentes = gigas_utilizados - plano_selecionado["limite_internet_gigas"]

        while gigas_excedentes > 0:
            valor_final += 10
            gigas_excedentes -= 1

        return valor_final
    else:
        print("Plano não encontrado!")
        return 0


plano = input(
    f"""
      == Planos ==
        - basico
        - intermediario
        - avancado

      Selecione um plano: """
)

minutos_telefonia_utilizados = int(
    input("Informe quantos minutos em ligações você utilizou no mês: ")
)

gigas_utilizados = int(
    input("Informe quantos gigas de internet você utilizou no mês: ")
)

mensagem = f"Valor da fatura: R$ {calcula_preco(plano, minutos_telefonia_utilizados, gigas_utilizados)}"

print(mensagem)

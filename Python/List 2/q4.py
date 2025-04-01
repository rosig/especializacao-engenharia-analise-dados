try:
    numero_infracoes = int(input("Escreva o número de infrações que você cometeu: "))
    categoria = ""

    # Talvez fique mais legível usar if / elif, mas a idéia foi experimentar coisas novas
    match numero_infracoes:
        case _ if numero_infracoes == 0:
            categoria = "Exemplar"
        case _ if numero_infracoes <= 3:
            categoria = "Atento"
        case _ if numero_infracoes >= 4 and numero_infracoes <= 6:
            categoria = "Desatento"
        case _:
            categoria = "Perigoso"

    print(f"Categoria: Motorista {categoria}")
except ValueError:
    print("Por favor, insira um número válido.")

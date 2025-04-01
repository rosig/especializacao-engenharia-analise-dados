dict_restaurantes = {}  # {(media, numero_avaliacoes)}
nome_restaurante = ""
restaurante_maior_nota = ("", 0.0)  # (nome, maior_nota)
restaurante_menor_nota = ("", float("inf"))  # (nome, menor_nota)

print("Digite PARE para finalizar!")

while nome_restaurante != "PARE":
    nome_restaurante = input("Nome do restaurante: ")

    if nome_restaurante != "PARE":
        nota_restaurante = int(input("Nota do restaurante (de 0 a 5): "))

        if dict_restaurantes.get(nome_restaurante, None):
            media_anterior = dict_restaurantes[nome_restaurante][0]
            numero_avaliacoes = dict_restaurantes[nome_restaurante][1]
            nova_media = ((media_anterior * numero_avaliacoes) + nota_restaurante) / (
                numero_avaliacoes + 1
            )
            dict_restaurantes[nome_restaurante] = (nova_media, numero_avaliacoes + 1)
        else:
            dict_restaurantes[nome_restaurante] = (nota_restaurante, 1)

        if nota_restaurante > restaurante_maior_nota[1]:
            restaurante_maior_nota = (nome_restaurante, nota_restaurante)

        if nota_restaurante < restaurante_menor_nota[1]:
            restaurante_menor_nota = (nome_restaurante, nota_restaurante)

print(
    f"Restaurante com a maior nota: {restaurante_maior_nota[0]} - Nota média: {dict_restaurantes[restaurante_maior_nota[0]][0]}"
)

print(
    f"Restaurante com a menor nota: {restaurante_menor_nota[0]} - Nota média: {dict_restaurantes[restaurante_menor_nota[0]][0]}"
)

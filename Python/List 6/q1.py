numeros_cores = int(input("Números de cores: "))
cores = []

for _ in range(numeros_cores):
    cores.append((input("Nome da cor: "), input("R: "), input("G: "), input("B: ")))

cor_selecionada = (input("Escreva o nome de uma cor: "), False)

for cor in cores:
    if cor[0] == cor_selecionada[0]:
        cor_selecionada = (cor_selecionada[0], True)
        print(
            f"Valores RGB para a cor {cor[0]}: Red={cor[1]}, Green={cor[2]}, Blue={cor[3]}"
        )
        break

if not cor_selecionada[1]:
    print(f"A cor {cor_selecionada[0]} não foi encontrada na lista.")

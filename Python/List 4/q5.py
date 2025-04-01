numero_vendedores = int(input("Qual é o número de vendedores? "))

vendedores = []


for _ in range(numero_vendedores):
    vendedores.append((input("Nome do vendedor: "), input("Total de vendas: ")))

vendedor_menor_volume_vendas = min(vendedores, key=lambda x: x[1])
vendedor_maior_volume_vendas = max(vendedores, key=lambda x: x[1])

for vendedor in vendedores:
    if vendedor[0] == vendedor_menor_volume_vendas[0]:
        print(f"{vendedor[0]}: {vendedor[1]} - Menor volume de vendas!")
    elif vendedor[0] == vendedor_maior_volume_vendas[0]:
        print(f"{vendedor[0]}: {vendedor[1]} - Maior volume de vendas!")
    else:
        print(f"{vendedor[0]}: {vendedor[1]}")

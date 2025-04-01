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

vendas = []
maior_venda = 0
menor_venda = float("inf")
mes_maior_venda = ""
mes_menor_venda = ""

for i in range(12):
    venda = float(input(f"Digite o valor das vendas de {meses[i]}: R$ "))
    vendas.append(venda)

    if venda > maior_venda:
        maior_venda = venda
        mes_maior_venda = meses[i]

    if venda < menor_venda:
        menor_venda = venda
        mes_menor_venda = meses[i]

total_vendas = sum(vendas)
media_vendas = total_vendas / len(meses)

print(f"\nMês com a maior venda: {mes_maior_venda} (R$ {maior_venda:.2f})")
print(f"Mês com a menor venda: {mes_menor_venda} (R$ {menor_venda:.2f})")
print(f"Média de vendas ao longo do ano: R$ {media_vendas:.2f}")
print(f"Total de vendas no ano: R$ {total_vendas:.2f}")

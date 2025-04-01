numero_clientes = int(input("Quantos clientes há na loja? "))

clientes_aptos = 0
total_bonus = 0

for _ in range(numero_clientes):
    nome = input("Nome do cliente: ")
    valor_compras = float(input("Valor total em compras do cliente: "))

    if valor_compras >= 2000:
        bonus = valor_compras * 0.15
        clientes_aptos += 1
        total_bonus += bonus
        print("Cliente apto para receber o bônus")

print(f"Clientes: {clientes_aptos}")
print(f"Total: R$ {total_bonus:.0f}")

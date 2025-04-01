numero_clientes = int(input("Digite o número de clientes na academia: "))
clientes = []

cliente_mais_alto = {"codigo": None, "altura": 0.0, "peso": 0.0}
cliente_mais_baixo = {"codigo": None, "altura": float("inf"), "peso": 0.0}
cliente_mais_pesado = {"codigo": None, "altura": 0.0, "peso": 0.0}
cliente_mais_leve = {"codigo": None, "altura": 0.0, "peso": float("inf")}

soma_alturas = 0
soma_pesos = 0

for _ in range(numero_clientes):
    codigo = int(input("Digite o código do cliente: "))
    altura = float(input("Digite a altura do cliente (em metros): "))
    peso = float(input("Digite o peso do cliente (em kg): "))

    clientes.append({"codigo": codigo, "altura": altura, "peso": peso})

    if altura > cliente_mais_alto["altura"]:
        cliente_mais_alto = {"codigo": codigo, "altura": altura, "peso": peso}

    if altura < cliente_mais_baixo["altura"]:
        cliente_mais_baixo = {"codigo": codigo, "altura": altura, "peso": peso}

    if peso > cliente_mais_pesado["peso"]:
        cliente_mais_pesado = {"codigo": codigo, "altura": altura, "peso": peso}

    if peso < cliente_mais_leve["peso"]:
        cliente_mais_leve = {"codigo": codigo, "altura": altura, "peso": peso}

    soma_alturas += altura
    soma_pesos += peso

media_altura = soma_alturas / numero_clientes
media_peso = soma_pesos / numero_clientes


print(
    f"O cliente mais alto tem: código {cliente_mais_alto['codigo']}, altura {cliente_mais_alto['altura']}m e peso {cliente_mais_alto['peso']}kg."
)
print(
    f"O cliente mais baixo tem: código {cliente_mais_baixo['codigo']}, altura {cliente_mais_baixo['altura']}m e peso {cliente_mais_baixo['peso']}kg."
)
print(
    f"O cliente mais leve tem: código {cliente_mais_leve['codigo']}, altura {cliente_mais_leve['altura']}m e peso {cliente_mais_leve['peso']}kg"
)
print(
    f"O cliente mais pesado tem: código {cliente_mais_pesado['codigo']}, altura {cliente_mais_pesado['altura']}m e peso {cliente_mais_pesado['peso']}kg."
)
print(f"A média das alturas é: {media_altura:.2f}")
print(f"A média dos pesos é: {media_peso}")

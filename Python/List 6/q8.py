print(
    f"""
      === Códigos === 
1. Incluir produto
2. Excluir produto
3. Atualizar estoque
4. Exibir todo o estoque
5. Calcular valor total do estoque
6. Sair
"""
)

estoque = {}  # {nome_produto: (quantidade, preco_unitario)}

codigo = int(input("Digite um código: "))

while codigo != 6:
    match codigo:
        case 1:
            nome = input("Produto: ")
            quantidade = int(input("Quantidade: "))
            preco_unitario = float(input("Preço unitário: "))
            estoque.update({nome: (quantidade, preco_unitario)})
            print(f"Produto '{nome}' adicionado ao estoque.")
        case 2:
            nome = input("Produto: ")
            produto = estoque.get(nome)

            if produto:
                estoque.pop(nome)
            else:
                print("Produto não encontrado!")
        case 3:
            nome = input("Produto: ")
            produto = estoque.get(nome)

            if produto:
                quantidade = int(input("Quantidade: "))
                estoque.update({nome: (quantidade, produto[1])})
                print(f"Estoque de '{nome}' atualizado para {quantidade} unidades.")
            else:
                print("Produto não encontrado!")
        case 4:
            print("Lista de Produtos em Estoque:")
            for nome_produto, (quantidade, preco_unitario) in estoque.items():
                print("Nome: ", nome_produto)
                print(f"Quantidade em Estoque: {quantidade} unidades")
                print(f"Preço Unitário: R$ {preco_unitario:.2f}")
        case 5:
            valor_total = 0
            for _, (quantidade, preco_unitario) in estoque.items():
                valor_total += quantidade * preco_unitario
            print(f"Valor total do estoque: R$ {valor_total:.2f}")

        case _:
            print("Código inválido!")

    codigo = int(input("Digite um código: "))

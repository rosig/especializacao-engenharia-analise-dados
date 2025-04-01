produto = ""
lista_produtos = []
quantidade = 0

while produto != "FIM":
    produto = input("Digite o nome do produto (digite FIM para sair): ")

    if produto != "FIM":
        quantidade = int(input("Digite a quantidade: "))

        if quantidade >= 0:
            lista_produtos.append(produto)
        elif quantidade < 0:
            print("Não é possível cadastro de estoque negativo.")

print(f"Tipos de produtos cadastrados: {len(lista_produtos)}")

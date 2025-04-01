lista_pessoas = []

while len(lista_pessoas) != 5:
    lista_pessoas.append(
        {
            "nome": input("Escreva o nome da pessoa: "),
            "idade": int(input("Escreva a idade: ")),
            "altura": float(input("Escreva a altura: ")),
        }
    )

pessoa_mais_alta = max(lista_pessoas, key=lambda pessoa: pessoa["altura"])

print(
    f"{pessoa_mais_alta['nome']}, com {pessoa_mais_alta['idade']} anos e {pessoa_mais_alta['altura']}m, é a pessoa mais alta do grupo."
)

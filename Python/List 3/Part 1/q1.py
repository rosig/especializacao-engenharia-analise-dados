idade = 0
lista_idades = []

while idade != -1:
    idade = int(input("Digite uma idade (digite -1 para sair): "))

    if idade != -1:
        lista_idades.append(idade)

quantidade_idades = len(lista_idades)

print(f"Total de idades: {quantidade_idades}")
print(f"Média das idades: {sum(lista_idades)/quantidade_idades}")
print(f"Maiores de 25 anos: {len([idade for idade in lista_idades if idade >= 25])}")
print(f"Menores de 25 anos: {len([idade for idade in lista_idades if idade < 25])}")

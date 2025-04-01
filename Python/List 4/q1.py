idades = []
input_idade = 0

print("Escreva -1 para sair.")

while input_idade != -1:
    input_idade = int(input("Escreva uma idade: "))

    if input_idade != -1:
        idades.append(input_idade)

print(f"Quantidade de idades válidas: {len(idades)}")
print(f"Idades armazenadas: {idades}")

media = sum(idades) / len(idades)

print(f"Média das idades: {media}")
print(
    f"Quant. de idades acima da média: {len([idade for idade in idades if idade > media])}"
)
print(f"Maior idade: {max(idades)}")
print(f"Menor idade: {min(idades)}")
print(
    f"Quant. de idades abaixo de 18: {len([idade for idade in idades if idade < 18])}"
)

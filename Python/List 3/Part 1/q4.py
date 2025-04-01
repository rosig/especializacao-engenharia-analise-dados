codigo_servico = 0

dict_contador_servico = {}

print(
    f"""
  = Códigos
  1 - banho
  2 - tosa
  3 - banho e tosa
  4- outros)
"""
)

while codigo_servico != -1:
    codigo_servico = int(input("Digite o código do serviço (digite -1 para sair): "))

    if codigo_servico in range(1, 5):
        dict_contador_servico[codigo_servico] = (
            dict_contador_servico.get(codigo_servico, 0) + 1
        )

print(f"Banho: {dict_contador_servico[1]}")
print(f"Tosa: {dict_contador_servico[2]}")
print(f"Banho e Tosa: {dict_contador_servico[3]}")
print(f"Outros: {dict_contador_servico[4]}")

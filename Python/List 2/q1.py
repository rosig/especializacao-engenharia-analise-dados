estados_civiles_dict = {"S": "Solteiro", "C": "Casado", "V": "Viúvo", "D": "Divorciado"}

primeira_letra_estado_civil = input("Escreva a primeira letra do seu estado civil: ")

try:
    mensagem = estados_civiles_dict[primeira_letra_estado_civil.upper()]
    print(mensagem)
except KeyError:
    print("Entrada inválida!")

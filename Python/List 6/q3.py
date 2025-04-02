NUMERO_DE_FUNCIONARIOS = 30

dict_escala_novembro = {}  # {dia: nome_funcionario}

for _ in range(NUMERO_DE_FUNCIONARIOS):
    nome_funcionario = input("Nome do funcionário: ")
    dia_plantao = None

    while dia_plantao == None:
        dia_plantao = int(input("Dia plantão:"))

        if dia_plantao == 0 or dia_plantao not in range(NUMERO_DE_FUNCIONARIOS + 1):
            print(f"Dia inválido! Digite um dia entre 1 e {NUMERO_DE_FUNCIONARIOS}")
            dia_plantao = None
        elif dict_escala_novembro.get(dia_plantao) != None:
            print(f"O dia {dia_plantao} já está ocupado!")
            dia_plantao = None
        else:
            dict_escala_novembro.update({dia_plantao: nome_funcionario})

escala_ordenada = [item for item in dict_escala_novembro.items()]
escala_ordenada.sort(key=lambda x: x[0])

tupla_plantao_dias_pares = ([], [])
tupla_plantao_dias_impares = ([], [])

for dia, nome_funcionario in escala_ordenada:
    if dia % 2 == 0:
        tupla_plantao_dias_pares[0].append(nome_funcionario)
        tupla_plantao_dias_pares[1].append(dia)
    else:
        tupla_plantao_dias_impares[0].append(nome_funcionario)
        tupla_plantao_dias_impares[1].append(dia)

print(
    f"""
Pessoas no plantão (dias pares): {tupla_plantao_dias_pares}
Pessoas no plantão (dias ímpares): {tupla_plantao_dias_impares}   
"""
)

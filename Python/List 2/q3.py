dict_dias_da_semana = {
    1: "Domingo",
    2: "Segunda",
    3: "Terça",
    4: "Quarta",
    5: "Quinta",
    6: "Sexta",
    7: "Sábado",
}

numero_dia_semana = int(input("Escreva um número correspondente ao dia da semana: "))

nome_dia_semanaa = dict_dias_da_semana.get(numero_dia_semana, "Valor inválido!")

print(nome_dia_semanaa)

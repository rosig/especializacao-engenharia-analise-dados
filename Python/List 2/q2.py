cargo_id = int(input("Escreva seu cargo na escola: "))
salario = float(input("Escreva seu salário: "))

percentual_aumento = 0

match cargo_id:
    case 1:
        percentual_aumento = 0.45
    case 2:
        percentual_aumento = 0.35
    case 3:
        percentual_aumento = 0.25
    case 4:
        percentual_aumento = 0.15
    case 5:
        percentual_aumento = 0

print(f"Salário atualizado: {salario * (1+percentual_aumento)}")

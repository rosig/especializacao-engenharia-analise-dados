print(
    f"""
      === Códigos === 
1. Criar uma nova conta
2. Consultar o saldo de uma conta específica
3. Realizar um saque em uma conta
4. Realizar um depósito em uma conta
5. Sair
"""
)

contas = {}  # {numero: {titular, saldo}}
codigo = int(input("Digite um código: "))

while codigo != 5:
    match codigo:
        case 1:
            numero_conta = int(input("Número da conta: "))
            conta = contas.get(numero_conta)

            if not conta:
                titular = input("Nome do titular: ")
                saldo = float(input("Saldo: "))
                contas.update({numero_conta: {"titular": titular, "saldo": saldo}})
                print("Conta criada com sucesso.")
            else:
                print("Já existe uma conta com esse número!")
        case 2:
            numero_conta = int(input("Número da conta: "))
            conta = contas.get(numero_conta)

            if conta:
                print(f"Saldo da conta: R$ {conta.get('saldo'):.2f}")
            else:
                print("Conta não encontrada!")
        case 3:
            numero_conta = int(input("Número da conta: "))
            conta = contas.get(numero_conta)

            if conta:
                valor_sacar = float(input("Valor a ser sacado: "))
                saldo_conta = conta.get("saldo")

                if saldo_conta >= valor_sacar:
                    conta["saldo"] -= valor_sacar
                    print("Saque realizado com sucesso.")
                else:
                    print("Saldo insuficiente.")
            else:
                print("Conta não encontrada!")
        case 4:
            numero_conta = int(input("Número da conta: "))
            conta = contas.get(numero_conta)

            if conta:
                valor_depositar = float(input("Valor a ser depositado: "))
                conta["saldo"] += valor_depositar
                print("Depósito realizado com sucesso.")
            else:
                print("Conta não encontrada!")
        case _:
            print("Código inválido!")

    codigo = int(input("Digite um código: "))

print("Programa finalizado.")

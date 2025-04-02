print(
    f"""
      === Códigos === 
1. Incluir contato
2. Excluir contato
3. Buscar contato
4. Sair.
"""
)

agenda = {}  # {nome: telefone}

codigo = int(input("Digite um código: "))

while codigo != 4:
    match codigo:
        case 1:
            nome = input("Nome: ")
            numero = int(input("Número: "))
            agenda.update({nome: numero})
            print("Contato adicionado com sucesso!")
        case 2:
            nome = input("Nome: ")
            numero = agenda.get(nome)

            if numero:
                agenda.pop(nome)
                print("Contato excluído com sucesso!")
            else:
                print("Contato não encontrado na agenda.")
        case 3:
            nome = input("Nome: ")
            numero = agenda.get(nome)

            if numero:
                print(f"Número de telefone de {nome}: {numero}.")
            else:
                print("Contato não encontrado na agenda.")
        case _:
            print("Código inválido!")

    codigo = int(input("Digite um código: "))

print("Agenda: ")
print(agenda)
print("Programa finalizado!")

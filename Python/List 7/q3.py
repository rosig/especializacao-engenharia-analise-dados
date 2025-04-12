agenda = {}  # {nome: telefone}


def incluir_contato(nome, telefone):
    global agenda
    agenda.update({nome: telefone})
    print("Contato adicionado com sucesso!")


def excluir_contato(nome):
    global agenda
    numero = agenda.get(nome)

    if numero:
        agenda.pop(nome)
        print("Contato excluído com sucesso!")
    else:
        print("Contato não encontrado na agenda.")


def buscar_contato(nome):
    global agenda
    numero = agenda.get(nome)

    if numero:
        print(f"Número de telefone de {nome}: {numero}.")
    else:
        print("Contato não encontrado na agenda.")


def main():
    print(
        f"""
        === Códigos === 
    1. Incluir contato
    2. Excluir contato
    3. Buscar contato
    4. Sair.
    """
    )

    codigo = int(input("Digite um código: "))

    while codigo != 4:
        match codigo:
            case 1:
                nome = input("Nome: ")
                numero = int(input("Número: "))
                incluir_contato(nome, numero)
            case 2:
                nome = input("Nome: ")
                excluir_contato(nome)
            case 3:
                nome = input("Nome: ")
                buscar_contato(nome)
            case _:
                print("Código inválido!")

        codigo = int(input("Digite um código: "))

    print("Agenda: ")
    print(agenda)
    print("Programa finalizado!")


main()

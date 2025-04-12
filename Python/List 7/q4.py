def atualizar_numeros(primeiro_dict, segundo_dict):
    for letra, _ in primeiro_dict.items():
        primeiro_dict.update({letra: segundo_dict.get(letra)})

    print(f"Os valores atualizados do primeiro dicionário são: {primeiro_dict}")


def main():
    numeros_maria = {"a": 100, "b": 200, "c": 300}
    numeros_sara = {"a": 300, "b": 200, "d": 400, "c": 500, "e": 250}
    atualizar_numeros(numeros_maria, numeros_sara)


main()

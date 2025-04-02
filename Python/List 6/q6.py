numeros_maria = {"a": 100, "b": 200, "c": 300}
numeros_sara = {"a": 300, "b": 200, "d": 400, "c": 500, "e": 250}

for letra, _ in numeros_maria.items():
    numeros_maria.update({letra: numeros_sara.get(letra)})

print(f"Os valores do dicionário numeros_maria são: {numeros_maria}")

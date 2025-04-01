lista_numeros = []

while len(lista_numeros) != 10:
    lista_numeros.append(int(input("Digite um número: ")))

maior_numero = max([numero for numero in lista_numeros if numero % 2 == 0])

print(f"Maior número par: {maior_numero}")

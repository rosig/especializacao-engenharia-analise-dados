numeros = []

for _ in range(10):
    numeros.append(int(input("Escreva um número: ")))

numeros_pares = []
numeros_impares = []

for numero in numeros:
    if numero % 2 == 0:
        numeros_pares.append(numero)
    else:
        numeros_impares.append(numero)

print(f"Números: {numeros}")
print(f"Pares: {numeros_pares}")
print(f"Ímpares: {numeros_impares}")

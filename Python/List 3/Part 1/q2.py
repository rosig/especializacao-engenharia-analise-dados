nota = 0
lista_notas = []

while nota != -1:
    nota = int(input("Digite uma nota entre 1 e 5 (digite -1 para sair): "))

    if nota in range(1, 6):
        lista_notas.append(nota)
    elif nota != -1:
        print("Nota inválida!")

print(f"Média das idades: {sum(lista_notas)/len(lista_notas)}")

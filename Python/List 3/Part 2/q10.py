primeiro_numero = int(input("Escreva o primeiro número da sequência: "))
segundo_numero = int(input("Escreva o segundo número da sequência: "))

sequencia = [primeiro_numero, segundo_numero]

for i in range(20):
    proximo_numero = sequencia[-1] + sequencia[-2]
    sequencia.append(proximo_numero)

print("Sequência:")
for numero in sequencia:
    print(numero)

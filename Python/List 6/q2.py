x1, y1, z1 = (float(input("x1: ")), float(input("y1: ")), float(input("z1: ")))
x2, y2, z2 = (float(input("x2: ")), float(input("y2: ")), float(input("z2: ")))
distancia = (((x2 - x1) ** 2) + ((y2 - y1) ** 2) + ((z2 - z1) ** 2)) ** 0.5
print(f"A distância entre os dois pontos é: {distancia:.2f}")

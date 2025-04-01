numero_celular = input("Número de celular: ")
prefix = ""

if (len(numero_celular) == 9 and numero_celular.find("-") != -1) or (
    len(numero_celular) == 8 and numero_celular.find("-") == -1
):
    prefix = "9"

print(prefix + numero_celular)

dict_square = {}

for num in range(15):
    num += 1
    dict_square.update({num: num**2})

# Outra solução
# dict_square = {(num + 1): (num + 1) ** 2 for num in range(15)}

print(dict_square)

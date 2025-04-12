def square(num):
    return {(item + 1): (item + 1) ** 2 for item in range(num)}


print(square(15))

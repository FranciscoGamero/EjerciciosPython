def encontrarNumeros():
    list_a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    list_b = [2, 7, 1, 12]
    numEncontrados = []
    for num in list_a:
        if num in list_b:
            numEncontrados.append((num, num))
    return tuple(numEncontrados)

print(encontrarNumeros())

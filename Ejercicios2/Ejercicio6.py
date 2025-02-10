def numComunes():
    lista1 = [1, 2, 3, 4]
    lista2 = [2, 3, 4, 5]
    numComunes = []
    for num in lista1:
        if num in lista2:
            numComunes.append(num)
    return numComunes

print(numComunes())
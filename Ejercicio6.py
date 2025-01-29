def compararArrays(arr1, arr2, comunes):
    result = []

    if comunes:
        for elem in arr1:
            if elem in arr2:
                result.append(elem)
    else:
        for elem in arr1:
            if elem not in arr2:
                result.append(elem)
        for elem in arr2:
            if elem not in arr1:
                result.append(elem)

    return result
arr1 = [1, 2, 3, 4, 5]
arr2 = [3, 4, 5, 6, 7]
print(compararArrays(arr1, arr2, True))
print(compararArrays(arr1, arr2, False))

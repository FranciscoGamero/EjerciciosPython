def encontrarNumeros():
    frase = 'En 1984 hubo 13 casos de protesta con más de 1000 asistentes'.split()
    listaNum = []
    for palabra in frase:
        if palabra.isnumeric():
            listaNum.append(palabra)
    return listaNum

print(encontrarNumeros())
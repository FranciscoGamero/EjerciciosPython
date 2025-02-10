def encontrarConsonantes():
    frase = 'A los yaks amarillos les gusta gritar y bostezar y ayer cantaban mientras comían ñames asquerosos'
    lista = frase.split(frase)
    resultado = []
    for palabra in lista:
        if palabra.lower() not in 'aeiouáéíóú':
            resultado.append(palabra)
    return resultado

print(encontrarConsonantes())
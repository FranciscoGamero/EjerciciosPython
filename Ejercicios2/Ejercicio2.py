def encontrarNumero():
    resultado = []
    num = range(1001)
    for n in num:
        if '3' in str(n):
            resultado.append(n)
    return resultado
print(encontrarNumero())
def encontrarDivisibles():
    resultado =  []
    num = range(1001)
    for i in num:
        if i%7==0:
            resultado.append(i)
    return resultado

print(encontrarDivisibles())
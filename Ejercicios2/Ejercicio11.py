def encontrarDivisibles():
    listaNumeros = [] 
    for num in range(1, 1001):
        for divisor in range(2, 10):
            if num % divisor == 0:
                listaNumeros.append(num)
                break
    return listaNumeros

print(encontrarDivisibles())

def ponerEnMayusculas(string):
    listaPalabras = string.split(" ")
    listaFinal = []
    for palabra in listaPalabras:
        palabraModificada = palabra[0].upper() + palabra[1:]
        listaFinal.append(palabraModificada)
    return " ".join(listaFinal)

print("Inserte una frase")
frase = str(input())
print(ponerEnMayusculas(frase))
def encontrarPalabrasMenores(frase):
    listaPalabras = [] 
    listaFrase = frase.split()
    for palabra in listaFrase:
        if len(palabra) < 4:
            listaPalabras.append(palabra)
    return listaPalabras

frase = 'Frase para probar la funcion'
print(encontrarPalabrasMenores(frase))

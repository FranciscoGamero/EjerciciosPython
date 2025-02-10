buenasMalas = {
    "Pelosos": 1,
    "Sureños buenos": 2,
    "Enanos": 3,
    "Númenóreanos": 4,
    "Elfos": 5
}

razasMalas = {
    "Sureños malos": 2,
    "Orcos": 2,
    "Goblins": 2,
    "Huargos": 3,
    "Trolls": 5
}

def calcularFuerzaEjercito(ejercito, valorRazas):
    fuerzaTotal = 0
    for raza, count in ejercito.items():
        fuerzaTotal += valorRazas.get(raza, 0) * count
    return fuerzaTotal

def batalla(ejercitoBien, ejercitoMal):

    fuerzaBien = calcularFuerzaEjercito(ejercitoBien, buenasMalas)
    fuerzaMal = calcularFuerzaEjercito(ejercitoMal, razasMalas)
    
    if fuerzaBien > fuerzaMal:
        return "El bien triunfa sobre el mal"
    elif fuerzaMal > fuerzaBien:
        return "El mal prevalece"
    else:
        return "La batalla termina en empate"

ejercitoBien = {
    "Pelosos": 3,
    "Elfos": 1,
    "Enanos": 2
}
ejercitoMal = {
    "Orcos": 1,
    "Trolls": 1
}

result = batalla(ejercitoBien, ejercitoMal)
print(result)

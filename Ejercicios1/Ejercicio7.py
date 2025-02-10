def comprobarGanador(listaJuegos):
    movimientosGanadores = {
        "R": "S",
        "S": "P",
        "P": "R"
    }

    jugador1 = 0
    jugador2 = 0

    for move1, move2 in listaJuegos:
        if move1 == move2:
           
            continue
        elif movimientosGanadores[move1] == move2:
            jugador1 += 1
        else:
            jugador2 += 1

    if jugador1 > jugador2:
        return "Jugador 1"
    elif jugador2 > jugador1:
        return "Jugador 2"
    else:
        return "Empate"
    
listaJuegos = [("R", "S"), ("S", "R"), ("P", "S")]
result = comprobarGanador(listaJuegos)
print(result)

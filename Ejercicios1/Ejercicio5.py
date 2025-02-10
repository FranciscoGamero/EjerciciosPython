def evaluarCarrera(acciones, pista):
    result_pista = list(pista)
    race_successful = True

    for i in range(len(pista)):
        if acciones[i] == "run" and pista[i] == "_":
            pass 
        elif acciones[i] == "jump" and pista[i] == "|":
            pass
        elif acciones[i] == "jump" and pista[i] == "_":
            result_pista[i] = "x"
            race_successful = False
        elif acciones[i] == "run" and pista[i] == "|":
            result_pista[i] = "/"
            race_successful = False

    print("".join(result_pista))

    return race_successful

acciones = ["run", "jump", "run", "jump", "run"]
pista = "_|_|_"
evaluarCarrera(acciones, pista)

acciones = ["run", "run", "run", "jump", "run"]
pista = "_|_|_"
evaluarCarrera(acciones, pista)

acciones = ["jump", "run", "run", "jump", "run"]
pista = "_|_|_"
evaluarCarrera(acciones, pista)

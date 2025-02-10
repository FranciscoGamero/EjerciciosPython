def comprobarBalanceado(expresion):
    guardar = []
    balanceado = True
    for caracter in expresion:
        if caracter in ["{", "(", "["]: 
            guardar.append(caracter)
        elif caracter in ["}", ")", "]"]:
            if not guardar:
                balanceado = False
                break
            tope = guardar.pop()
            if (caracter == "}" and tope != "{") or (caracter == ")" and tope != "(") or (caracter == "]" and tope != "["):
                balanceado = False
    
    if not balanceado:
        return "La expresión: "+ expresion +" no es balanceada"
    
    return f"La expresión: {expresion} es balanceada"

# Prueba interactiva
print("Introduzca la expresión:")
expresion = input()

print(comprobarBalanceado(expresion))

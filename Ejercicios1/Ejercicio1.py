morse = {
    "._": "A",
    "_...": "B",
    "_._.": "C",
    "_..": "D",
    ".": "E",
    ".._.": "F",
    "__.": "G",
    "....": "H",
    "..": "I",
    ".___": "J",
    "_._": "K",
    "._..": "L",
    "__": "M",
    "_.": "N",
    "___": "O",
    ".__.": "P",
    "__._": "Q",
    "._.": "R",
    "...": "S",
    "_": "T",
    ".._": "U",
    "..._": "V",
    ".__": "W",
    "_.._": "X",
    "_.__": "Y",
    "__..": "Z"
}

abecedario = {
    "A": "._",
    "B": "_...",
    "C": "_._.",
    "D": "_..",
    "E": ".",
    "F": ".._.",
    "G": "__.",
    "H": "....",
    "I": "..",
    "J": ".___",
    "K": "_._",
    "L": "._..",
    "M": "__",
    "N": "_.",
    "O": "___",
    "P": ".__.",
    "Q": "__._",
    "R": "._.",
    "S": "...",
    "T": "_",
    "U": ".._",
    "V": "..._",
    "W": ".__",
    "X": "_.._",
    "Y": "_.__",
    "Z": "__.."
}

def traducir_a_morse(texto):
    texto = texto.upper()
    morse_text = ""
    for letra in texto:
        if letra == " ":
            morse_text += " / " 
        else:
            morse_text += abecedario[letra] + " "
    return morse_text.strip() 

def traducir_a_texto(textoMorse):
    texto = ""
    letras = textoMorse.strip().split(" ")
    for letra in letras:
        if letra in morse:
            texto += morse[letra]
        elif letra == "/":
            texto += " "
    return texto

print("Introduzca el texto que quiera traducir:")
texto = input()

if texto[0] == "." or texto[0] == "_":
    print(traducir_a_texto(texto))
else:
    print(traducir_a_morse(texto))

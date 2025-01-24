def comprobarCaracteres(str1, str2):
    out1 = []
    out2 = []
    for character in str1 :
        if character not in str2:
            out1.append(character)
    for character in str2:
        if character not in str1:
            out2.append(character)
    return out1, out2

print("Inserte un texto")
str1= input()
print("Inserte otro texto")
str2= input()

print(comprobarCaracteres(str1,str2))



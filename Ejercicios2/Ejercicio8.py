def encontrarPares():
    numbers = range(20)
    for num in numbers:
        if num%2==0:
            print("par")
        else:
            print("impar")

encontrarPares()
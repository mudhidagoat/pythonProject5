while True:
    try:
        num1 = float(input("skriv det første nummer: "))
        op = input("skriv dit regneform: ")
        num2 = float(input('skriv det andet nummer: '))

        if op == "+":
            print(num1 + num2)
        elif op == "-":
            print(num1 - num2)
        elif op == "/":
            print(num1 / num2)
        elif op == "*":
            print(num1 * num2)
        else:
            print(" vælg en gyldig regneform ")

    except ValueError:
        print("Vælg et gyldigt tal")
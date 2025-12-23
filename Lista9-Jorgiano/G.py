while True:
    sentenca = input().lower().split()
    primeira_letra = sentenca[0][0]

    if sentenca[0] == "*":
        break

    else:
        tautograma = True
        for i in sentenca:
            if i[0] != primeira_letra:
                tautograma = False
                break
            else:
                tautograma = True

        if tautograma:
            print("Y")
        else:
            print("N")
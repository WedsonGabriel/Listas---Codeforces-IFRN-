while True:
    n1, n2 = input().split()

    if n1 == '0' and n2 == '0':
        break

    while len(n1) > 1:
        soma = 0
        for digito in n1:
            soma += int(digito)
        n1 = str(soma)

    while len(n2) > 1:
        soma = 0
        for digito in n2:
            soma += int(digito)
        n2 = str(soma)

    if int(n1) > int(n2):
        print(1)
    elif int(n2) > int(n1):
        print(2)
    else:
        print(0)
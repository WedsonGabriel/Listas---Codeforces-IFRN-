while True:
    try:
        h1, m1, h2, m2 = map(int,input().split())

        if (h1 == 0) and (m1 == 0) and (h2 == 0) and (m2 == 0):
            break

        tempo_atual = (h1*60) + m1
        tempo_alarme = (h2*60) + m2

        diferenca = tempo_alarme - tempo_atual

        if diferenca < 0:
            diferenca += 1440

        print(diferenca)

    except EOFError:
        break
       


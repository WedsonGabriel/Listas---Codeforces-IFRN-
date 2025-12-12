while True:
    qtd_testes = int(input())

    if qtd_testes == 0:
        break

    seq_magnitudes = list(map(int,input().split()))
    picos = 0

    for i in range(qtd_testes):
        indice_esquerda = (i - 1) % qtd_testes
        indice_direita = (i + 1) % qtd_testes

        if (seq_magnitudes[i] > seq_magnitudes[indice_esquerda]) and (seq_magnitudes[i] > seq_magnitudes[indice_direita]):
            picos += 1
        if (seq_magnitudes[i] < seq_magnitudes[indice_esquerda]) and (seq_magnitudes[i] < seq_magnitudes[indice_direita]):
            picos += 1

    print(picos)

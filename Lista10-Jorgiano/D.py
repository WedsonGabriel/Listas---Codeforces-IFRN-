n = int(input())
numeros = []

for i in range(n):
    numeros.append(int(input()))
resposta = 1

for i in range(n):
    for j in range(i+1, n):
        if numeros[j] == numeros[i]:
            continue
        atual = numeros[i]
        proximo = numeros[j]
        resposta_atual = 2
        for k in range(j+1, n):
            if numeros[k] == atual:
                resposta_atual += 1
                atual, proximo = proximo, atual
        if resposta_atual > resposta:
            resposta = resposta_atual
print(resposta)
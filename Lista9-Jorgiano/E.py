caracteres = int(input())
sequencia =  input()

monotonos = 0
tamanho_atual = 1

for i in range(len(sequencia)-1):
    if sequencia[i] == sequencia[i+1]:
        tamanho_atual += 1
    else:
        if sequencia[i] == "a" and tamanho_atual >= 2:
            monotonos += tamanho_atual

        tamanho_atual = 1

if sequencia[-1] == "a" and tamanho_atual >= 2:
    monotonos += tamanho_atual

print(monotonos)

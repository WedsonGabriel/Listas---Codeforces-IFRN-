jogadas = int(input())
vitorias = 0

for car in range(jogadas):
    porta_carro = int(input())

    if porta_carro != 1:
        vitorias += 1

print(vitorias)

qtd_jogadores, qtd_rodadas = map(int, input().split())
pontos = list(map(int, input().split()))

total = [0] * qtd_jogadores

jogador = 0
for i in range(len(pontos)):
    total[jogador] += pontos[i]
    jogador = (jogador + 1) % qtd_jogadores

vencedor = 0
for i in range(len(total)):
    if total[i] >= total[vencedor]:
        vencedor = i

print(vencedor + 1)
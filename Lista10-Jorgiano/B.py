qtd_competidores, pontos_minimos = map(int, input().split())
lista_pontos_jogadores = []
convidados = 0 

for pontos in range(qtd_competidores):
    f1, f2 = map(int, input().split()) #pontuação do jogador
    soma_pontos = f1 + f2
    lista_pontos_jogadores.append(soma_pontos)

for analise in lista_pontos_jogadores:
    if analise >= pontos_minimos:
        convidados += 1

print(convidados)
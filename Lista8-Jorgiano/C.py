pulo_sapo , qtd_canos = map(int,input().split())
altura_canos = list(map(int,input().split()))
perdeu = False

for jump in range(qtd_canos - 1):
    diferenca = abs(altura_canos[jump + 1] - altura_canos[jump])

    if diferenca > pulo_sapo:
        perdeu = True
        break

if perdeu:
    print("GAME OVER")
else:
    print("YOU WIN")
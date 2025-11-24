c= int(input())

saldo_atual = 100
maior_premio = 100

for game in range(c):
    conteudo = int(input())

    saldo_atual += conteudo

    if saldo_atual > maior_premio:
        maior_premio = saldo_atual

print(maior_premio)
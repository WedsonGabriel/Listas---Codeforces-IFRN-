quantidade_pilhas = int(input())
entrada = input().split()

pilhas = []
for numero in entrada:
    pilhas.append(int(numero))

total_pedras = 0
for pedra in pilhas:
    total_pedras += pedra

soma_base = (quantidade_pilhas * (quantidade_pilhas - 1)) // 2

resto = total_pedras - soma_base

if resto < 0 or resto % quantidade_pilhas != 0:
    print("-1")
else:
    altura_inicial = resto // quantidade_pilhas
    
    if altura_inicial <= 0:
        print("-1")
    else:
        movimentos = 0
        for i in range(quantidade_pilhas):
            altura_desejada = altura_inicial + i
            if pilhas[i] > altura_desejada:
                movimentos += pilhas[i] - altura_desejada
        
        print(movimentos)



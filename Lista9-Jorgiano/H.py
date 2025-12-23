tamanho = int(input())
sequencia = list(map(int,input().split()))

if tamanho <= 2:
    print("1")
    
else:
    quantidade_escadinhas = 1
    diferenca_atual = sequencia[1] - sequencia[0]

    for i in range(2,tamanho):
        nova_diferenca = sequencia[i] - sequencia[i-1]

        if nova_diferenca != diferenca_atual:
            quantidade_escadinhas += 1
            diferenca_atual = nova_diferenca

    print(quantidade_escadinhas)
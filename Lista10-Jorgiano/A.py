vendas = 0
estoque_total = []

qtd_tamanhos_disponíveis = int(input())
for estoque in range(qtd_tamanhos_disponíveis):
    estoque_modelo = int(input())
    estoque_total.append(estoque_modelo)

qtd_pedidos_recebidos = int(input())
for pedidos in range(qtd_pedidos_recebidos):
    tamanho_chinelo_pedido = int(input())

    indice = tamanho_chinelo_pedido - 1

    if estoque_total[indice] > 0 and indice <= len(estoque_total) - 1:
        estoque_total[indice] -= 1
        vendas += 1

print(vendas)
    
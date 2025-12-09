qtd_testes = int(input())

for buy in range(qtd_testes):
    orcamento, qtd_marcas = map(int,input().split())
    valor_marca = list(map(float,input().split()))
    maior_troco = 0.0

    for buy in valor_marca:
        if buy <= orcamento:
            troco_atual = orcamento % buy

            if troco_atual > maior_troco:
                maior_troco = troco_atual
        
    print(f"{maior_troco:.2f}")


qtd_medicoes = int(input())
lista_bc = []

for i in range(qtd_medicoes):
    valor_bc = int(input())
    lista_bc.append(valor_bc)

media = sum(lista_bc) // qtd_medicoes

quantidade = 0

for i in lista_bc:
    if i > int(media * 1.1):
        quantidade += 1

    if i < int(media * 0.9):
        quantidade += 1

print(media)
print(quantidade)


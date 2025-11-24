quantidade = int(input())
numeros = list(map(int, input().split()))

media= sum(numeros)/quantidade

qtd_menores= 0
qtd_maiores= 0

for numero in numeros:
    if numero < media:
        qtd_menores += 1
    if numero >= media:
        qtd_maiores += 1

print(f"{media:.1f}")
print(qtd_menores)
print(qtd_maiores)
       
quantidade = int(input())
numeros = list(map(int, input().split()))

media = sum(numeros)/quantidade

qtd_menores = 0
qtd_maiores = 0
seletor_menor = []
seletor_maior = []

for numero in numeros:
    if numero < media:
        qtd_menores += 1
    if numero < media:
        seletor_menor.append(numero)
    if numero >= media:
        qtd_maiores += 1
    if numero >= media:
        seletor_maior.append(numero)

print(f"{media:.1f}")
print(qtd_menores, *seletor_menor)
print(qtd_maiores, *seletor_maior)
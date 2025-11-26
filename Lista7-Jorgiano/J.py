tamanho = int(input())
lista= []
qtd_seq = 0

for sequencia in range(tamanho):
    numbers= int(input())
    lista.append(numbers)

for i in range(tamanho-1):
    if lista[i] != lista[i+1]:
        qtd_seq += 1

print(qtd_seq + 1)
dna_sequence = input()

tamanho_maximo = 1
comprimento_atual = 1

for i in range(1, len(dna_sequence)):
    if dna_sequence[i] == dna_sequence[i-1]:
        comprimento_atual += 1
    else:
        comprimento_atual = 1

    if comprimento_atual > tamanho_maximo:
        tamanho_maximo = comprimento_atual
        
print(tamanho_maximo)


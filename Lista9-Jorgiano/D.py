mensagem = input()
crib = input()

tam_msg = len(mensagem)
tam_crib = len(crib)
contagem = 0

for i in range(tam_msg - tam_crib + 1):
    valido = True
    for j in range(tam_crib):
        if mensagem[i + j] == crib[j]:
            valido = False
            break
    
    if valido:
        contagem += 1

print(contagem)
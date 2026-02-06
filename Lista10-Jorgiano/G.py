tabuleiro = []
for i in range(10):
    linha_vazia = []
    for j in range(10):
        linha_vazia.append(0)
    tabuleiro.append(linha_vazia)

posicionamento_valido = True

quantidade_navios = int(input())

for navio in range(quantidade_navios):
    entrada = input().split()
    
    direcao = int(entrada[0])
    comprimento = int(entrada[1])
    linha = int(entrada[2])
    coluna = int(entrada[3])

    indice_linha = linha - 1
    indice_coluna = coluna - 1

    if linha > 10 or coluna > 10:
        posicionamento_valido = False

    if direcao == 0:
        if coluna + comprimento - 1 > 10:
            posicionamento_valido = False
        
        if posicionamento_valido:
            for k in range(comprimento):
                if tabuleiro[indice_linha][indice_coluna + k] == 1:
                    posicionamento_valido = False
                
                tabuleiro[indice_linha][indice_coluna + k] = 1

    else:
        if linha + comprimento - 1 > 10:
            posicionamento_valido = False
            
        if posicionamento_valido:
            for k in range(comprimento):
                if tabuleiro[indice_linha + k][indice_coluna] == 1:
                    posicionamento_valido = False
                
                tabuleiro[indice_linha + k][indice_coluna] = 1

if posicionamento_valido:
    print('Y')
else:
    print('N')
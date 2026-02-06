quantidade_numeros = int(input())
entrada = input().split()
sequencia = []

for numero in entrada:
    sequencia.append(int(numero))

if quantidade_numeros <= 2:
    print(1)
else:
    partes = 1
    razao_atual = sequencia[1] - sequencia[0]
    i = 2
    
    while i < quantidade_numeros:
        diferenca = sequencia[i] - sequencia[i-1]
        
        if diferenca == razao_atual:
            i = i + 1
            
        else:
            partes = partes + 1
            i = i + 1
            
            if i < quantidade_numeros:
                razao_atual = sequencia[i] - sequencia[i-1]
                i = i + 1

    print(partes)
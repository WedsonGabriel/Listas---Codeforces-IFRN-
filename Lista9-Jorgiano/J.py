qtd_competidores = int(input())
min_classificados = int(input())
pontos_competidores = []

for i in range(qtd_competidores):
    pontos = int(input())
    pontos_competidores.append(pontos)

ordem_pontos = sorted(pontos_competidores, reverse = True) 
nota_corte = ordem_pontos[min_classificados - 1]
classificados = 0

for n in ordem_pontos:
    if n >= nota_corte:
        classificados += 1
    else:
        break

print(classificados)






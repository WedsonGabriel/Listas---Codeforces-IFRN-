qtd_voluntarios, qtd_sobreviventes = map(int,input().split())
voluntarios_sobreviventes = list(map(int,input().split()))
voluntarios_mortos = []

for i in range(1, qtd_voluntarios + 1):
    if i not in voluntarios_sobreviventes:
        voluntarios_mortos.append(i)

if len(voluntarios_sobreviventes) == qtd_voluntarios:
    print("*")

print(*voluntarios_mortos, "")


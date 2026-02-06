n = int(input())
fita = list(map(int, input().split()))

distancia = n 
for i in range(n):
    if fita[i] == 0:
        distancia = 0
    else:
        distancia += 1
        fita[i] = distancia

distancia = n
for i in range(n - 1, -1, -1):
    if fita[i] == 0:
        distancia = 0
    else:
        distancia += 1
        if distancia < fita[i]:
            fita[i] = distancia

for i in range(n):
    if fita[i] > 9:
        fita[i] = 9

print(*fita)


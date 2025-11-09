n1, d1, v1 = map(int, input().split())
n2, d2, v2 = map(int, input().split())

tempo_charrete1= d1/v1
tempo_charrete2= d2/v2

if (tempo_charrete1) < (tempo_charrete2):
    print(n1)
else:
    print(n2)

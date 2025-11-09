f,b,m= map(int, input().split()) #Número de refeições disponíveis
fp,bp,mp= map(int, input().split()) #Número de refeições requisitadas

falta_f=0
falta_b=0
falta_m=0

if (fp>f):
    falta_f= abs(f-fp)
if (bp>b):
    falta_b= abs(b-bp)
if (mp>m):
    falta_m= abs(m-mp)

falta_geral= falta_f + falta_b + falta_m
print(falta_geral)
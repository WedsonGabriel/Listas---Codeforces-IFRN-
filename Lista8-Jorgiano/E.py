qtd_testes = int(input())

for food in range(qtd_testes):
    c = float(input())
    dias = 0
    while c > 1.0:
        c = c / 2
        dias += 1
    print(f"{dias} dias")




    


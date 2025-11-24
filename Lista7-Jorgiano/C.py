a,b= map(int,input().split())

for multiplos in range(1, b+1):
    resultado = a * multiplos
    
    if resultado > b:
        break
    print(resultado, end=" ")


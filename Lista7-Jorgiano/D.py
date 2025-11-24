n = int(input())

for divisores in range(1, n+1):
    if n % divisores == 0:
        print(divisores, end=" ")
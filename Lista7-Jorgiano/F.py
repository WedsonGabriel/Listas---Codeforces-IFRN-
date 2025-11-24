def primo(n):
    if n <= 1:
        return False
    
    for p in range(2, n):
        if n % p == 0:
            return False
    
    return True

n = int(input())

if primo(n):
    print("Sim")
else:
    print("Nao")
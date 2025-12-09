def primo(n):
    if n <= 1:
        return False

    for p in range(2, n):
        if n % p == 0:
            return False
        
    return True

number = int(input())        
maior_primo = number + 1


while not primo(maior_primo):
    maior_primo += 1

print(maior_primo)
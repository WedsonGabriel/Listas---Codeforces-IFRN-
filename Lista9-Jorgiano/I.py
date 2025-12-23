teste = 1

while True:
    n = int(input())
    
    if n == 0:
        break
        
    max_x = -10001
    min_y = 10001
    min_u = 10001
    max_v = -10001
    
    for i in range(n):
        x, y, u, v = map(int, input().split())
        
        if x > max_x: max_x = x
        if y < min_y: min_y = y
        if u < min_u: min_u = u
        if v > max_v: max_v = v
        
    print(f"Teste {teste}")
    
    if max_x < min_u and max_v < min_y:
        print(f"{max_x} {min_y} {min_u} {max_v}")
    else:
        print("nenhum")
        
    print()
    teste += 1
sa_size, sb_size = map(int, input().split())
sequence_a = list(map(int, input().split()))
sequence_b = list(map(int, input().split()))

indice_b = 0

for i in sequence_a:
    if indice_b < sb_size:
        if i == sequence_b[indice_b]:
            indice_b += 1
    else:
        break

if indice_b == sb_size:
    print("S")
else:
    print("N")


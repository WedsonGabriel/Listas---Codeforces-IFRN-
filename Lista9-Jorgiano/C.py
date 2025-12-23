qtd_vezes = int(input())
interruptor = list(map(int,input().split()))
l1 = 0
l2 = 0

for i in interruptor:
    if i == 1:
        l1 = int(not l1)
    elif i == 2:
        l1 = int(not l1)
        l2 = int(not l2)

print(l1)
print(l2)

# ---------------------------------------------------------------------------------------------------------------------------

# OUTRA ALTERNATIVA
# qtd_vezes = int(input())
# interruptor = list(map(int,input().split()))
# l1 = 0
# l2 = 0

# for i in interruptor:
#     if i == 1:
#         if l1 == 0:
#             l1 = 1
#         else:
#             l1 = 0
        
#     if i == 2:
#         if l1 == 0:
#             l1 = 1
#         else:
#             l1 = 0

#         if l2 == 0:
#             l2 = 1
#         else:
#             l2 = 0

# print(l1)
# print(l2)
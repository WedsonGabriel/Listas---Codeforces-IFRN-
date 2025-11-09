c= int(input())
d= int(input())
t= int(input())

necessário= (d/c)-t

if necessário <=0:
    necessário=0
    
print(f'{necessário:.1f}')
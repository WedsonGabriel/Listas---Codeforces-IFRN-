a= int(input())
b= int(input())
c= int(input())
d= int(input())

dif1= abs((a+b) - (c+d))
dif2= abs((a+c) - (b+d))
dif3= abs((a+d) - (b+c))

if dif1<=dif2 and dif1<=dif3:
    menor= dif1
elif dif2<=dif1 and dif2<=dif3:
    menor= dif2
elif dif3<=dif1 and dif3<=dif2:
    menor= dif3

print(menor)

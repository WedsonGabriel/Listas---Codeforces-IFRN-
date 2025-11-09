a,b,c,d= map(int, input().split())

abc= (a+b>c) and (a+c>b) and (b+c>a)
abd= (a+b>d) and (a+d>b) and (b+d>a)
acd= (a+c>d) and (a+d>c) and (c+d>a)
bcd= (b+c>d) and (b+d>c) and (c+d>b)

if (abc==True) or (abd==True) or (acd==True) or (bcd==True):
    print("S")
else:
    print("N")   
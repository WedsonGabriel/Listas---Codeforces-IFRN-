a=int(input())
b=int(input())
c=int(input())

#se a for a irmã do meio
if (a>=b and a<=c) or (a<=b and a>=c):
    print(a)
#se b for a irmã do meio
elif (b>=a and b<=c) or (b<=a and b>=c):
    print(b)
#se c for a irmã do meio
elif (c>=a and c<=b) or (c<=a and c>=b):
    print(c)




a,b,c= map(int, input().split())

if (a>=b) and (a>=c):
    m1= a
    m2= b
    m3= c
elif (b>=a) and (b>=c):
    m1= b
    m2= a
    m3= c
elif (c>=a) and (c>=b):
    m1= c
    m2= a
    m3= b


if not (m1 < (m2+m3)):
    print("n")
elif (m1**2 == m2**2+m3**2):
    print("r")
elif (m1**2 > m2**2+m3**2):
    print("o")
elif (m1**2 < m2**2+m3**2):
    print("a")
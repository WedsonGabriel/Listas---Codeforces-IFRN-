a11, a21= map(int, input().split()) #avaliação1
a12, a22= map(int, input().split()) #avaliação2
p1, p2= map(int, input().split()) #pesos
 
m1= (a11*p1 + a21*p2)//(p1+p2)
m2= (a12*p1 + a22*p2)//(p1+p2)
 
if (m1>m2):
    print("1")
elif (m1<m2):
    print("2")
elif (m1==m2):
    print("1")
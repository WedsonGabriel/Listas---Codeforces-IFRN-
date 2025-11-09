l= int(input()) #Linhas
c= int(input()) #Colunas
 
if (l%2==0) and (c%2==0):
    print('1')
elif (l%2==1) and (c%2==1):
    print('1')
elif (l%2==1) and (c%2==0):
    print('0')
elif (l%2==0) and (c%2==1):
    print('0')


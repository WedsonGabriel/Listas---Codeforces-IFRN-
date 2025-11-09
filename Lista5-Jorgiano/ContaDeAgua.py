n= int(input())

if (n<=10):
    valor_pago= 7
elif (11<=n<=30):
    valor_pago= 7+(n-10)*1
elif (31<=n<=100):
    valor_pago= 7+20+(n-30)*2
elif (n>=101):
    valor_pago= 7+20+140+(n-100)*5

print(valor_pago)


num=int(input("enter a number"))
cub=0
while(num>0):
    mod=num%10
    cub+=mod*mod*mod
    num//=10
print(cub)
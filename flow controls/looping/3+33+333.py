num=int(input("enter a number"))
h=0

for i in range(1,num+1):
    a=str(num)*i
    h+=int(a)
print(h)

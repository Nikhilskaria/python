num1=int(input("enter a number"))
num2=int(input("enter a number"))
num3=int(input("enter a number"))
if(num1>num2)&(num1>num3):
    print(num1,"is greater")
elif(num2>num1)&(num2>num3):
    print(num2, "is greater")
elif(num1==num2)&(num2==num3):
    print("numbers are equal")
else:
    print(num3, "is greater")


num1=int(input("enter a number"))
num2=int(input("enter a number"))
num3=int(input("enter a number"))
if(num1>num2&num1<num3)|(num1>num3&num1<num2):
    print(num1, "is 2nd largest")
elif(num2>num3&num2<num3)|(num2>num1&num2<num3):
    print(num2, "is 2nd largest")
elif(num1==num2)&(num2==num3):
    print("numbers are same")
else:
    print(num3,"is 2nd largest")
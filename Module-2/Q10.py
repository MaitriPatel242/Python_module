a=int(input("Enter number1: "))
b=int(input("Enter number2: "))
flag=True
if a==b or a+b==5 or a-b==5:
    flag=True
else:
    flag=False
print(flag)
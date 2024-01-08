#with temp
a= int(input("Enter a: "))
b= int(input("Enter b: "))
temp=a
a=b
b=temp
print(a,b)

#without temp
a= int(input("Enter a: "))
b= int(input("Enter b: "))
a,b=b,a
print(a,b)
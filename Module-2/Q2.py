n= int(input("Enter number: "))
n1=n
fect=1
while n>0:
    fect*=n
    n-=1
    print(fect)
print(f"Fectorial of {n1} is {fect}")
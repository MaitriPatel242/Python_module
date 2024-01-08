n= int(input("Enter number: "))
a,b=0,1
cnt=0
while cnt<n:
    print(a)
    c=a+b
    a=b
    b=c
    cnt+=1

str= input("Enter String: ")
cnt=0
for i in str:
    if i.islower() or i.isupper():
        cnt+=1
print(cnt)
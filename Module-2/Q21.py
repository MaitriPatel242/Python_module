str= input("Enter String: ")
str1=""
if len(str)%4==0:
    str1= str[::-1]
    print(str1)
else:
    print(str)
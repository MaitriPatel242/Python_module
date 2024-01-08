str= input("Enter string: ")
if len(str)>2:
    print(str[0:2]+str[len(str)-2:])
else:
    print("")
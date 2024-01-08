def insertmid():
    str= input("Enter String: ")
    str1= input("Enter String to insert: ")
    ans= str[0:int(len(str)/2)]+str1[:]+str[int(len(str)/2):]
    print(ans)
insertmid()
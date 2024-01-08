str= input("Enter String: ")
poorindex=str.find("poor")
notindex=str.find("not")
str1=""
if poorindex<notindex:
    str1=str[:poorindex]+"good"+str[notindex+3:]
    print(str1)
str = input("Enter string: ")
if len(str)>3:
    if (str[-3:-1]=='in' and str[-1]=='g'):
        str1= str[:]+"ly"
    else:
        str1= str[:]+"ing"
print(str1)
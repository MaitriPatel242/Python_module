string1=input("Enter string1: ")
string2=input("Enter string2: ")
newstring=string1[1]+string1[0]+string1[2:len(string1)+1]+" "+string2[1]+string2[0]+string2[2:len(string2)+1]
print(newstring)
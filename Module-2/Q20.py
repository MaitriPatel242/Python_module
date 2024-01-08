li = eval(input("Enter list: "))
maxlen = len(li[0])  
for item in li:
    if len(item) > maxlen:
        maxlen = len(item)

print("Longest element length:", maxlen)

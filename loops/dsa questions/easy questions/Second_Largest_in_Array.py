a = [12,14,13,1244,222,1]
temp = 0
for i in a:
    if i > temp:
        temp = i
a.remove(temp)
temp2 = 0
for  i in a:
    if i > temp2:
        temp2 = i
print("Second largest number is:",temp2)
#A strong number (also known as a Krishnamurthy number or factorion) is a positive integer that is equal to the sum of the factorials of its individual digits. 
n = 145
sum = 0
for i in str(n):
    product = 1
    for j in range(1,int(i)+1):
        product *= j
    sum += product

if sum == n:
    print(n, "is a Strong Number")
else:
    print(n, "is not a Strong Number")
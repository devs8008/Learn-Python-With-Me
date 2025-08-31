n = 1634
lengths = len(str(n))
sum = 0
for i in str(n):
    sum += int(i)**lengths
if sum == n:
    print(n,"is an Armstrong number")
else:
    print(n,"is not an Armstrong number")
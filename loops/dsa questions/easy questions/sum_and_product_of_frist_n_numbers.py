n = 10
sum = 0
product = 1
for i in range(1, n + 1):
    product *= i
    sum += i
print("The sum of first", n, "numbers is:", sum)
print("The sum of first", n, "numbers is:", product)
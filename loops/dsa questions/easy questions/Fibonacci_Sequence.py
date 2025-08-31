# Fibonacci sequence using loop
n = 10  # number of terms

print("Fibonacci Sequence:")
a,b = 0,1
for i in range(n):
    print(a,end = ' ')
    a,b = b,a+b


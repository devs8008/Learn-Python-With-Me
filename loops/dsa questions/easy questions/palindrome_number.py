palindrome = 1221
reversei = []
for i in str(palindrome):
    reversei.append(i)
reversei.reverse()
reversed_str = "".join(reversei)
if str(palindrome) == reversed_str:
    print("Palindrome")
else:
    print("Not a Palindrome")
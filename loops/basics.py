#Python has two main types of loops:
    #for loop – iterate over sequences (list, string, tuple, dict, range, etc.)
    #while loop – repeat until a condition becomes False

#There’s also loop control statements: break, continue, pass, and else with loops.



#1. for loop
for i in range(5):  # 0 to 4
    print(i)

for i in range(2, 6):  # 2,3,4,5
    print(i)

for i in range(0, 10, 2):  # 0,2,4,6,8
    print(i)

#Iterating over a list
fruits = ["apple", "banana", "cherry"]  
for fruit in fruits:
    print(fruit)

#Iterating over a string
for char in "hello":
    print(char)



#2. while loop
i = 1
while i <= 5:
    print(i)
    i += 1
#Note: Be careful to avoid infinite loops!



#3. Loop control statements

#break statement
for i in range(10):
    if i == 5:
        break  # exit the loop when i is 5
    print(i)

#continue statement
for i in range(10):
    if i % 2 == 0:
        continue  # skip even numbers
    print(i)

#pass statement
for i in range(5):
    if i == 3:
        pass  # do nothing, just a placeholder
    print(i)

#else with loops
for i in range(5):
    print(i)
else:
    print("Loop completed without break")   

#5. Nested Loops
for i in range(3):
    for j in range(2):
        print(f"i: {i}, j: {j}")

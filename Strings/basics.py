#1
# sytax for defining strings in Python
a = "It's alright" # use double quotes if string contains single quote

b = 'He is called Johnny"' # use single quotes if string contains double quote

# use triple quotes for multi-line strings
c = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""

#2
#Strings are Arrays
a = "Hello, World!"
print(a[1])
#Strings are Arrays of bytes representing unicode characters

#3
#Looping through a string
for x in "banana":
  print(x)  
#Note: When looping through a string, the loop variable (x in this example). Meaing x will be assigned the value of each character in the string one by one, and we can use x to perform operations with each character inside the loop.


#4
#String Length
a = "Hello, World!"
print(len(a))
#Note: The len() function returns the length of a string, which is the number of characters it contains, including spaces and punctuation.

#5 A.
#Check String
txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")
#Note: The 'in' keyword is used to check if a substring exists within a string. If the substring is found, the condition evaluates to True, and the code inside the if block is executed.

#5 B.
#Check if NOT
txt = "The best things in life are free!"
print("expensive" not in txt)

#6 
#Accessing Characters
s = "Python"
print(s[0])    # P (first character)
print(s[-1])   # n (last character)
print(s[2:5])  # tho (slice)
print(s[:3])   # Pyt
print(s[3:])   # hon

#7
#String Operations

#7 A.
#Concatenation
a = "Hello"
b = "World" 
c = a + " " + b
print(c)  # Hello World

#7 B.
#Repetition
d = "Ha" * 3
print(d)  # HaHaHa

#7 C.
#Membership
e = "H" in a
print(e)  # True
if "W" not in a:
  print("W is not in a")  # W is not in a

#8 
#String Methods
s = "  hello world  "

print(s.upper())      # "  HELLO WORLD  "
print(s.lower())      # "  hello world  "
print(s.title())      # "  Hello World  "
print(s.strip())      # "hello world" (removes spaces)
print(s.replace("world", "Python"))  # "  hello Python  "
print(s.split())      # ['hello', 'world']
print("-".join(["a", "b", "c"]))     # "a-b-c"
print(s.find("world")) # 8
print(s.count("l"))    # 3
print(s.startswith("  he"))  # True
print(s.endswith("ld  "))    # True

#9
#f-Strings
name = "Alice"
age = 30
print(f"My name is {name} and I am {age}")
print(f"2 + 2 = {2+2}")

#10
#Escape Characters
print("Hello\nWorld")   # Newline
print("Hello\tWorld")   # Tab
print("He said \"Hi\"") # Quotes inside
print("C:\\path")       # Backslash
print(r"C:\new\path")  # C:\new\path #Raw string (ignores escapes)

#11
#String Immutability
s = "Python"
# s[0] = "J"  ❌ Error
s = "J" + s[1:]  # ✅ "Jython"

#12
#Checking String Type
s = "123"
print(s.isdigit())   # True
print(s.isalpha())   # False
print(s.isalnum())   # True
print(" ".isspace()) # True
print("Hello".islower()) # False
print("HELLO".isupper()) # True












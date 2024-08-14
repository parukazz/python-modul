# In programming you often need to know if an expression is True or False

print(10 > 9)
print(10 == 9)
print(10 < 9)

a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

# Evaluate Values and Variables

# The bool() function allows you to evaluate any value, and give you True or False in return

print(bool("Hello"))
print(bool(15))

# Evaluate two variables
x = "Hello"
y = 15

print(bool(x))
print(bool(y))

# Most Values are True

# Almost any values is evaluated to True if it has some sort of content
# Any string is True, except empty strings
# Any number is True, except 0
# Any list, tuple, set, and dictionary are True, except empty ones

bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])

# Some Values are False

bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})
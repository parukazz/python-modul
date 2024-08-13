x = 5
y = 10
z = 2

text = "Hello"
my_name = "Paruk Azziyi"
my_another_name = 'Xavier'

print(my_name)
print(x)
print(y)
print(z)
print(text)
print(my_another_name)

# case-sensitive
# a and A is different - A will not overwrite a

# Variable Names
"""
  short variable names = x, y, z, etc
  descriptive names = age, carname, total_volume

  Rules for Python varibles:
    - A variable name must start with a letter or the underscore character (using snake_case)
    - A variable name ~cannot~ start with a number
    - A variable name can only contain alpha-numeric characters and underscores -> A-z, 0-9, and _
    - Variable names are case-sensitive -> age, Age and AGE are three different variables
    - A variable name ~cannot~ be any of the Python keywords -> logical operators. define function, etc
"""

# Camel Case -> myVariable
# Pascal Case -> MyVariable
# Snake Case -> my_variable

# Many Values to Multiple Variables
a, b, c = "a", "b", "c"
print(a)
print(b)
print(c)

# One Value to MUltiple Variables
d = e = f = "Alphabet"
print(e)
print(f)

# Unpack a Collection
fruits = ["apple", "banana", "cherry"]
fruit_1, fruit_2, fruit_3 = fruits
print(fruit_2)

# Output Variables
print(d)
print(d, e, f)
print(fruit_1 + " " + fruit_2 + " " + fruit_3)

# Global Variables

# Variables that are created outside of a function (as in all of the examples in the previous pages) are known as global variables.

# Global variables can be used by evryone, both inside of functions and outside

value_1 = "awesome"
def my_func():
  print("Python is", value_1)

my_func()

# Local Variables

def my_func_2():
  value_1 = "so simple"
  print("Python is", value_1)

my_func_2()

# Global keyword

def my_func_3():
  global value_3
  value_3 = "amazing"

my_func_3()

print("Python is", value_3)
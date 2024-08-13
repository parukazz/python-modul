import random

# 3 types numeric in python
# int, float, complex

x = 1 # int
y = 2.8 # float
z = 2j # complex

# INT / INTEGER

# is a whole number, positive or negative, without decimals, of unlimited length

x = 42986
w = -32525235235

print(x)

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

# Random Number
print(random.randrange(1, 50))
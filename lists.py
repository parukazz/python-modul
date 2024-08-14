# Lists

mylist = ["apple", "banana", "cherry"]

# List like Array in another programming language

# Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.

thislist = ["apple", "banana", "cherry"]
print(thislist)

# Allow Duplicates
# since lists are indexed, lists can have items with the same value

thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)

thislist = ["apple", "banana", "cherry"]
print(len(thislist))

list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
print(list1)
print(list2)
print(list3)

list1 = ["abc", 34, True, 40, "male"]
print(list1)

# The list() Constructor

# It is also possible to use the list() constructor when creating a new list

thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)
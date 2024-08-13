# Data Types

# Built-in Data Types
# Python has the following data types built-in by default, in these categories:

"""
  - Text type: str
  - Numeric types: int, float, complex
  - Sequence types: list, tuple, range
  - Mapping type: dict
  - Set types: set, frozenset
  - Boolean type: bool
  - Binary types: bytes, bytearray, memoryview
  - None type: NoneType
"""

# this syntax for checking the type of data
x = 10
print(type(x))

# Types of Data in Python
str_type = "Hello World"
int_type = 20
float_type = 20.5
complex_type = 1j
list_type = ["apple", "banana", "cherry"]
tuple_type = ("apple", "banana", "cherry")
range_type = range(10)
dict_type = {
  "name" : "Paruk",
  "age" : 21
}
set_type = {
  "apple",
  "banana",
  "cherry"
}
frozenset_type = frozenset({
  "apple", "banana", "cherry"
})
bool_type = True
bytes_type = b"Hello"
bytearray_type = bytearray(5)
memoryview_type = memoryview(bytes(5))
none_type = None

print(str_type)
print(int_type)
print(float_type)
print(complex_type)
print(list_type)
print(tuple_type)
print(range_type)
print(dict_type)
print(set_type)
print(frozenset_type)
print(bool_type)
print(bytes_type)
print(bytearray_type)
print(memoryview_type)
print(none_type)
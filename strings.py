# Strings

# 'hello' is the same as "hello"

# Quotes Inside Quotes
print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')

# Assign String to a Variable
a = "Hello"
print(a)

# Multiline Strings
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

# Or useing three single quotes

# Strings are Arrays
"""
  Like many other popular programming languages, strings in Python are arrays of bytes representing unicode characters.

  However, Python does not have a character data type, a single character is simply a string with a length of 1.
"""

a = "Hello, World!"
print(a[1]) # result is e (H -> 0, e -> 1, l -> 2, and so on)

# Looping Through a String
for x in "banana":
  print(x) # result is b a n a n a (column direction)

# String Length
a = "Hello, Wolrd!"
print(len(a))

# Check String
txt = "The best things in life are free!"
print("free" in txt) # result is True

txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")

txt = "The best things in life are free!"
print("expensive" not in txt)

txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")


# Slicing
b = "Hello, World!"
print(b[2:5]) # result is llo, take string from index 2 to index 4

# Negative Indexing
b = "Hello, World!"
print(b[-5:-2])

# F-Strings
age = 36
txt = f"My name is John, I am {age}"
print(txt)

txt = "We are the so-called \"Vikings\" from the north."


"""
\'	Single Quote	
\\	Backslash	
\n	New Line	
\r	Carriage Return	
\t	Tab	
\b	Backspace	
\f	Form Feed	
\ooo	Octal value	
\xhh	Hex value
"""


class Person:
  def __init__(self, name, age, gender):
    self.name = name
    self.age = age
    self.gender = gender
    
    
__first = Person("Jurin", 22, "female")
__second = Person("Chisa", 23, "female")
__third = Person("Hinata", 22, "female")
__fourth = Person("Harvey", 22, "female")
__fifth = Person("Juria", 20, "female")
__sixth = Person("Maya", 19, "female")
__seventh = Person("Cocona", 18, "female")

print(__first.name, __first.age, __first.gender)
print(__second.name, __second.age, __second.gender)
print(__third.name, __third.age, __third.gender)
print(__fourth.name, __fourth.age, __fourth.gender)
print(__fifth.name, __fifth.age, __fifth.gender)
print(__sixth.name, __sixth.age, __sixth.gender)
print(__seventh.name, __seventh.age, __seventh.gender)

# Instance Methods

# functions that you define inside a class and can only call on an instance of that class.

class Members:
  def __init__(self, name, age):
    self.name = name
    self.age = age
    
  # instance method
  def description(self):
    return f"{self.name} is {self.age} years old"
  
  def position(self, role):
    self.role = role
    return f"{self.name} in XG as a {self.role}"
  
jurin = Members(
  "Asaya Jurin",
  22
)

desc = jurin.description()
role = jurin.position("Leader")

print()
print("====================")
print()

print(desc)
print(role)
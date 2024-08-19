# INHERITANCE

class Dog:
  species = "Canis familiaris"
  
  def __init__(self, name, age, breed):
    self.name = name
    self.age = age
    self.breed = breed
    
  def __str__(self):
    return f"{self.name} is {self.age} years old"
  
  def speak(self, sound):
    return f"{self.name} says {sound}"
  
miles = Dog("Miles", 4, "Jack Russell Terrier")
buddy = Dog("Buddy", 9, "Dachshund")
jack = Dog("Jack", 3, "Bulldog")
jim = Dog("Jim", 5, "Bulldog")

print(buddy.speak("Yap"))
print(jim.speak("Woof"))
print(jack.speak("Woof"))

class Dogs:
  species = "Canis familiaris"
  
  def __init__(self, name, age):
    self.name = name
    self.age = age
    
  def __str__(self):
    return f"{self.name} is {self.age} years old"
  
  def speak(self, sound):
    return f"{self.name} says {sound}"

class JackRussellTerrier(Dogs):
  pass

class Dachshund(Dogs):
  pass

class Bulldog(Dogs):
  pass

miles = JackRussellTerrier("Miles", 4)
buddy = Dachshund("Buddy", 9)
jack = Bulldog("Jack", 3)
jim = Bulldog("Jim", 5)

print(miles.species)
print(buddy.name)
print(jack)
print(jim.speak("Woof"))
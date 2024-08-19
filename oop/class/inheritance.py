class Parent:
  hair_color = "brown"
  speaks = ["Javanese"]
  
class Child(Parent):
  hair_color = "purple"
  def __init__(self):
    super().__init__()
    self.speaks.append("Sundanese")
print("\n\n ***** All Classes *****\n")

class Animal:

  def __init__(self, name):
    self.name = name
    self.age = 0
  
  def get_description(self):
    print(f"\n{self.name} is {self.age} years old")

  def walk(self):
    print(f"{self.name} is walking")

  def eat(self):
    print(f"{self.name} is eating")

class Cow(Animal):

  def __init__(self, name, milk_capacity):
    super().__init__(name)
    self.milk_capacity = milk_capacity

  def get_description(self):
    super().get_description()
    print(f"{self.name} can give {self.milk_capacity} ltrs milk")

  


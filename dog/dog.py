class Dog:
  def __init__(self, name, breed):
    self.name = name
    self.breed = breed
    print("Dog initialized!")

  def bark(self):
        print("Woof!")

# Create a Dog object with name and breed
my_dog = Dog("Moonlight", "Labrador")
print(my_dog.name)  # Print the name attribute
print(my_dog.breed)  # Print the breed attribute

# Call the bark method to make the dog bark
my_dog.bark()

# Create another Dog object
my_other_dog = Dog("Starshine", "SuperDog")
print(my_other_dog.name)

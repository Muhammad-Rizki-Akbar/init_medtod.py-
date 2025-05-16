class Dog:
    species = "Raviel"  # Class attribute

    def __init__(self, name, age):
        self.name = name  # Instance attribute
        self.age = age  # Instance attribute

dog1 = Dog("Rizki", 3)  # Create an instance of Dog
dog2 = Dog("Rizkan", 5)  # Create another instance of Dog

print(dog1.name, dog1.age, dog1.species)  # Access instance and class attributes
print(dog2.name, dog2.age, dog2.species)  # Access instance and class attributes
print(Dog.species)  # Access class attribute directly

class Dog:
    # Class variable
    species = "Raviel"

    def __init__(self, name, age):
        # Instance variables
        self.name = name
        self.age = age

# Create objects
dog1 = Dog("Rizki", 3)
dog2 = Dog("Rizkan", 5)

# Access class and instance variables
print(dog1.species)  # (Class variable)
print(dog1.name)     # (Instance variable)
print(dog2.name)     # (Instance variable)

# Modify instance variables
dog1.name = "cipi"
print(dog1.name)     # (Updated instance variable)

# Modify class variable
Dog.species = "capa"
print(dog1.species)  # (Updated class variable)
print(dog2.species)  

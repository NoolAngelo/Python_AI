# Define a class named 'Person'
class Person:
    # Constructor method to initialize the object
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Method to display the person's details
    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")

# Create an instance of the 'Person' class
person1 = Person("John", 25)

# Call the 'display_details' method to display the person's details
person1.display_details()
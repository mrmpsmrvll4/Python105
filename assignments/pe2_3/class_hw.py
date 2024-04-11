"""

Your task is to design and implement a class in a programming language. This class will represent a person and hold personal data.

Assignment Steps:
-----------------
1. Class Creation: Design a class named Person that includes the following data: name, address, age, and phone number.

2. Accessor and Mutator Methods: Write get and set methods for each piece of data. These methods allow you to access and change the data safely.

3. Creating Instances: Write a program that creates three instances (objects) of the Person class. Use one instance for your made-up information and the other two for imaginary friends or family members.

4. Display Data: Print out the information stored in each instance. Ensure the output is formatted and easy to read.

"""

# Class definition for a Student


class Person:
    # Initializer with private variables
    def __init__(self, name, address, age, phone_number):
        self.__name = name  # Private variable for name
        self.__address = address    # Private variable for address
        self.__age = age # Private variable for age
        self.__phone_number = phone_number   # Private variable for phone number
        
     # Method to get student's info as a formatted string
    def get_info(self):
        return f"Name: {self.__name}, Address: {self.__address}, Age: {self.__age}, Phone Number: {self.__phone_number}"

      # Getter for name
    def get_name(self):
        return self.__name

    # Getter for address
    def get_address(self):
        return self.__address
    
    # Getter for age
    def get_age(self):
        return self.__age

    # Getter for phone number
    def get_age(self):
        return self.__phone_number
    

    # Setter for name
    def set_name(self, name):
        self.__name = name

    # Setter for address
    def set_address(self, address):
        self.__address = address
    
    # Setter for age
    def set_age(self, age):
        self.__age = age

    # Setter for phone number
    def set_phone_number(self, phone_number):
        self.__phone_number = phone_number


# Set instances (objects) for class

def main():
    person1 = Person("Max", "1234 Street", "27", "867-5309")
    person2 = Person("Jax", "5678 Avenue", "28", "123-4567")
    person3 = Person("Dax", "9999 Boulevard", "29", "987-6543")

    # Show the info for each instance
    print("\n\n\n\n")
    print(person1.get_info())
    print(person2.get_info())
    print(person3.get_info())
    print("\n\n\n\n")

    # Show use of setter method as example
    person3.set_name("Quacks")
    person3.set_address("7777 Duck Lane")
    person3.set_age("7")
    person3.set_phone_number("777-7777")
    print(person3.get_info())


main()

"""
    creating our first class
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




def main():
    person1 = Person("Max", "1234 Street", "27", "867-5309")
    person2 = Person("Jax", "5678 Avenue", "28", "123-4567")
    person3 = Person("Dax", "9999 Boulevard", "29", "987-6543")

    print("\n\n\n\n")
    print(person1.get_info())
    print(person2.get_info())
    print(person3.get_info())
    print("\n\n\n\n")

    person3.set_name("Quacks")
    person3.set_address("7777 Duck Lane")
    person3.set_age("7")
    person3.set_phone_number("777-7777")
    print(person3.get_info())


main()

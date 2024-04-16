"""

Objective: Understand and implement a class with specific attributes and methods, and explore Python's special methods and functions.

Task Description:
1. Create the Pet Class:
    - Define a Pet class with attributes: kind (e.g., dog, cat), breed, and name.
    - Implement get and set methods for each of these attributes.
    - Add a method called print_details that prints the details of the pet.

2. Create Instances:
    - Create three objects of the Pet class with different kinds, breeds, and names.

    - Call the print_details method for each object that you created

3. Demonstrate a Special Method or Function:
-Choose one of the following and demonstrate its use with the Pet class instances:

    - __name__: Display the name of the class.
    - type(): Show the class used to instantiate a pet object.
    - __module__: Return the module name in which the Pet class is defined.
    - __bases__: Display the base classes of the Pet class (if any).
    - getattr(): Use it to access an attribute of a Pet instance.
    - isinstance(): Check if an instance is of the Pet class.

"""

# Class definition

class Pet:

    def __init__(self, kind, breed, name="Sparky"):
        # Instance variables
        self.__kind = kind
        self.__breed = breed
        self.__name = name


    # Setup getters
        
    def get_kind(self):
        return self.__kind
    
    def get_breed(self):
        return self.__breed
    
    def get_name(self):
        return self.__name
    
    
    # Setup setters

    def set_name(self, value):
        self.__kind = value
    
    def set_name(self, value):
        self.__breed = value

    def set_name(self, value):
        self.__name = value


    # Method to print pet details
        
    def print_details(self):
        print("Print Details:", vars(self))
    
    
    # Method to print basic info
        
    def print_info(self):
        print(self.__kind)
        print(self.__breed)
        print(self.__name)

# applying the class to a main function

def main():

    # making objects
    pet1 = Pet("Dog", "Lab", "Barky")
    pet2 = Pet("Cat", "Calico", "Keykey")
    pet3 = Pet("Duck" "Mallard", "Quack")

    # print pet1 details
    print("\n\n\n")
    pet1.print_details()
    pet1.print_info()

    # print pet2 details
    print("\n\n\n")
    pet2.print_details()
    pet2.print_info()

    # print pet3 details
    print("\n\n\n")
    pet3.print_details()
    pet3.print_info()

    # demonstrating the name method
    print("\n\n")
    print(pet1.__class__.__name__)

# calling main 
main()
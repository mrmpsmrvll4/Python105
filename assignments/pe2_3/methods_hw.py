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

4. Submission Requirements:
    - Submit the Python script containing the Pet class definition and instances by uploading it to your GitHub repository and submitting the link
    - Include comments to demonstrate the usage of the chosen special method or function.
    - Ensure code follows Python best practices for readability and efficiency.

"""

# Class definition
class Pet:
    
    def __init__(self, owner_first_name, owner_last_name, pet_id, pet_name, pet_type="Dog"):
        # Instance variables
        self.__owner_first_name = owner_first_name
        self.__owner_last_name = owner_last_name
        self.__pet_id = pet_id
        self.__pet_name = pet_name
        self.__pet_type = pet_type
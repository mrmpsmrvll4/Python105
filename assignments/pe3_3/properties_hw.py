# Class definition
class Pet:
    # Class variable
    school_name = "McHenry County College"

    def __init__(self, owner_first_name, owner_last_name, pet_id, pet_name, pet_type="Dog"):
        # Instance variables
        self.__owner_first_name = owner_first_name
        self.__owner_last_name = owner_last_name
        self.__pet_id = pet_id
        self.__pet_name = pet_name
        self.__pet_type = pet_type

    # Getter and Setter for first_name
    def get_owner_first_name(self):
        return self.__owner_first_name
    
    def get_owner_last_name(self):
        return self.__owner_last_name
        
    def get_pet_id(self):
        return self.__pet_id
    
    def get_pet_name(self):
        return self.__pet_name
    
    def get_pet_type(self):
        return self.__pet_type

    def set_owner_first_name(self, value):
        self.__owner_first_name = value
    
    def set_owner_last_name(self, value):
        self.__owner_last_name = value

    def set_pet_id(self, value):
        self.__pet_id = value
    
    def set_pet_name(self, value):
        self.__pet_name = value

    def set_grade_level(self, value):
        self.__pet_type = value

    # Method to print student details
    def print_pet_details(self):
        print("Pet Details:", vars(self))
    
    # Method to print basic info about the student
    def print_info(self):
        print(self.__owner_first_name + " " + self.__owner_last_name)
        print(self.__pet_id)
        print(self.__pet_name)
        print(self.__pet_type)

# Main function to demonstrate usage of the Student class
def main():
    # Creating an instance of Student
    pet_owner = Pet("Max", "Somerville", '8675309', "Gertrude", "Kitty")
    print("\n\n\n")
    print(pet_owner.get_owner_first_name())
    pet_owner.print_pet_details()
    pet_owner.print_info()

    print("\n\n\n")
    pet_owner.set_pet_name("Satan")
    pet_owner.print_info()

# Calling the main function
main()
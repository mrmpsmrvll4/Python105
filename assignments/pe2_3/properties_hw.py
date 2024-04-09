# Class definition
class Pet:
    # Class variable
    vet_name = "Pet Vet Clinic"


    def __init__(self, owner_first_name, owner_last_name, pet_id, pet_name, pet_type="Dog"):
        # Instance variables
        self.__owner_first_name = owner_first_name
        self.__owner_last_name = owner_last_name
        self.__pet_id = pet_id
        self.__pet_name = pet_name
        self.__pet_type = pet_type


    # Getter for first_name
    def get_owner_first_name(self):
        return self.__owner_first_name
    
    # Getter for last_name
    def get_owner_last_name(self):
        return self.__owner_last_name
        
    # Getter for pet_id
    def get_pet_id(self):
        return self.__pet_id
    
    # Getter for pet_name
    def get_pet_name(self):
        return self.__pet_name
    
    # Getter for pet_type
    def get_pet_type(self):
        return self.__pet_type
    

    # Setter for first_name
    def set_owner_first_name(self, value):
        self.__owner_first_name = value

    # Setter for last_name    
    def set_owner_last_name(self, value):
        self.__owner_last_name = value

    # Setter for pet_id
    def set_pet_id(self, value):
        self.__pet_id = value
    
    # Setter for pet_name
    def set_pet_name(self, value):
        self.__pet_name = value

    # Setter for pet_type
    def set_grade_level(self, value):
        self.__pet_type = value


    # Method to print pet details
    def print_pet_details(self):
        print("Pet Details:", vars(self))
    
    
    # Method to print basic info
    def print_info(self):
        print(self.__owner_first_name + " " + self.__owner_last_name)
        print(self.__pet_id)
        print(self.__pet_name)
        print(self.__pet_type)


# Main function to demonstrate usage of the Pet class
def main():
    # Creating an instance of Student
    pet_owner1 = Pet("Max", "Somerville", '8675309', "William", "Cat")
    pet_owner2 = Pet("Jax", "Jomerville", "1234567", "Quacks", "Duck")
    pet_owner3 = Pet("Dax", "Domerville", "9876543", "Lady", "Dog")

    print("\n\n\n")
    print(pet_owner1.get_owner_first_name())
    pet_owner1.print_pet_details()
    pet_owner1.print_info()

    print("\n\n\n")
    pet_owner2.set_pet_name("Scratchy")
    pet_owner2.print_info()

    print("\n\n\n")
    pet_owner3.print_info()

# Calling the main function
main()
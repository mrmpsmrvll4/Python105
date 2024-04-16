"""

Assignment Part 1: Defining Classes
-----------------------------------
File 1: Write an Employee class with the following attributes:
    - Employee name
    - Employee number
    - Create a subclass named ProductionWorker that inherits from Employee. 
        - This subclass should include additional attributes:
            - Shift number (integer: 1 for day, 2 for night)
            - Hourly pay rate

    - Implement accessor and mutator methods (getters and setters) for each class.


Assignment Part 2: Implementing and Testing
 -------------------------------------------

Part 2: Write a script to:

    - Create an instance of ProductionWorker.
    - Prompt the user for each attribute's data.
    - Store and then display the data using the object's methods.

"""
# make a class

class Employee:

    def __init__(self, employee_name, employee_number):
       
        self.__employee_name = employee_name
        self.__employee_number = employee_number

    # set getters
    def get_employee_name(self):
        return self.__employee_name
    
    def get_employee_number(self):
        return self.__employee_number
    
    # set setters
    def set_employee_name(self, value):
        self.__employee_name = value
    
    def set_employee_number(self, value):
        self.__employee_number = value

# make a subclass
class Productionworker:

    # added shift number and hourly pay rate to class
    def __init__(self, employee_name, employee_number, shift_number, hourly_pay_rate):

        super().__init__(self, employee_name, employee_number)
        self.shift_number = shift_number
        self.hourly_pay_rate = hourly_pay_rate

# make function to have production worker and ask for info and store and display data
def main():
    print



# call the main function
main()      
"""

Assignment: Inheritance


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
    def __str__(self):
        return "\n\nName: " + self.__employee_name + "\nEmployee number: " + self.__employee_number

# make a subclass
class Productionworker(Employee):

    # added shift number and hourly pay rate to class
    def __init__(self, employee_name, employee_number, shift_number, hourly_pay_rate):

        super().__init__(employee_name, employee_number)
        self.__shift_number = shift_number
        self.__hourly_pay_rate = hourly_pay_rate

        # set getters
    def get_shift_number(self):
        return self.__shift_number
    
    def get_hourly_pay_rate(self):
        return self.__hourly_pay_rate
    
    # set setters
    def set_shift_number(self, value):
        self.__shift_number = value
    
    def set_hourly_pay_rate(self, value):
        self.__hourly_pay_rate = value

    def __str__(self):
        return super().__str__() + " \nShift Number: " + self.__shift_number + "\nPay rate: " + self.__hourly_pay_rate


# make function to have production worker and ask for info and store and display data
def main():
    name = input("Enter a name: ")
    number = input("Enter your employee number (please enter a 1 or 2).: ")
    shift = input("Enter your shift number.: ")
    pay = input("Enter your hourly pay.: ")
    worker = Productionworker(name, number, shift, pay)
    print(worker)



# call the main function
main()      
"""

Assignment:
-----------
Ticket Sales


Objective: 
----------
Develop a program to manage ticket sales for an event.


Context: 
--------
You are in charge of ticket sales for a special event. 
The venue has 20 seats, each uniquely numbered from 1 to 20. 
Your task is to create a system that tracks and updates the availability of seats as they are sold.


Assignment Steps:
-----------------
1. Initialize the Seating List:
    - Create a list in your program representing the 20 seats. 
        This list should initially include all seat numbers (1-20).

2. Display Available Seats:
    - Write code to display the list of available seats to the customer. 
        This list should update as seats are sold.

3. Implement the Ticket Purchase Process:
    - Prompt the customer to select a seat by entering its number.
    - Include instructions in your prompt, indicating that the customer should enter '0' to finish their purchase.

4. Update Seat Availability:
    - Once a seat is selected, remove it from the list of available seats.
    - After each selection, display the updated list of available seats.
    - Continue this process until the customer enters '0', 
        indicating they are done buying tickets.

5. Ensure User-Friendly Interaction:
    - Your program should handle inputs gracefully. 
        If a customer selects a seat that doesn't exist or is already sold, 
            display a friendly message and prompt them to choose again.

6. Test Your Program:
    - Run your program to ensure it works as expected. 
        Try different scenarios, such as selling all seats, selling a few seats, and entering invalid seat numbers.


"""

#set the list for tickets to sell
seats = list(range(1, 21))

# show the open seats
print("Available Seats: ")
print(seats)

# buying a ticket
while True:
    chosen_seat = input("Enter what seat you want to buy, enter '0' when you've picked your seat: ")

    # set print for when done buying a ticket
    if chosen_seat == '0':
        print("You have successfully bought your ticket")
        break

    chosen_seat = int(chosen_seat)

    # seat availability
    if chosen_seat in seats:
        seats.remove(chosen_seat)
        print(f"Your seat {chosen_seat} has been purchased.")
    else:
        print("This seat isn't open, select another seat.")
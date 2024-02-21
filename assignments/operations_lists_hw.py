# set the list for tickets to sell
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

    chosen_seat = int(chosen_seat)

    # seat availability
    if chosen_seat in seats:
        seats.remove(chosen_seat)
        print(f"Your seat {chosen_seat} has been purchased.")
    else:
        print("This seat isn't open, select another seat.")
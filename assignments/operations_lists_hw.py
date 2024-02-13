def display_available_seats(seats):
    print("Available seats:")
    print(seats)

def main():
    # Initialize the list of available seats
    available_seats = list(range(1, 21))

    print("Welcome to the Ticket Sales System")

    while True:
        display_available_seats(available_seats)

        # Prompt the user to select a seat
        selected_seat = input("Please select a seat number (1-20), or enter '0' to finish: ")

        # Check if the input is valid
        if selected_seat == '0':
            print("Thank you for using our system. Have a great day!")
            break
        try:
            selected_seat = int(selected_seat)
            if selected_seat not in available_seats:
                print("Sorry, that seat is not available or does not exist. Please choose another seat.")
            else:
                # Remove the selected seat from available seats
                available_seats.remove(selected_seat)
                print(f"Seat {selected_seat} has been booked.")
        except ValueError:
            print("Invalid input. Please enter a valid seat number (1-20) or '0' to finish.")

if __name__ == "__main__":
    main()
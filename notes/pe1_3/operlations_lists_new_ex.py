# create list
seats = [1, 2, 3, 4, 5]

# display list
print("\n")
print("Enter the number of the seat that you wish to purchase")
print("When you are done enter 0")

done = 1

while done != 0:
    for seat in seats:
        print(seat, end=" ")
    buy = int (input("\nPlease enter the number of the seat you want to buy:  "))
    if buy == 0:
        print("Thanks for your purchase. \n Goodbye!")
        break
    elif buy in seats:
        seats.remove(buy)
    else:
        print("That is not an available seat")

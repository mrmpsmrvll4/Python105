# other functions would come at the top

# define a function to get a list of items for esater and the type of basket
def get_list(name):
    # set flag to true to start the loop
    flag = True
    # initialize an empty list to hold items for the easter basket
    easter_basket = []
    # greet the user with their name
    print(f"Hi! (name)!")
    # prompt the user to enter items for the easter basket
    print(" Please enter 'full' when you are done. ")
    # start a loop to coninuously get items until the user enters 'full'
    while flag:
        # prompt the user to enter a type of candy or toy for easter
        candy = input("What kind of candy or toy do you want for Easter:  ")
        # check if the user wants to stop entering items
        if candy == 'full':
            # if the user adds full exit the loop
            break
        # add the entered candy/toy to the easter basket list
        easter_basket.append(candy)
    # prompt the user to enter the type of basket they want
    basket = input("what kind of basket do you want? (plastic, wood, et.):  ")
    # return the list of items for the easter basket and the type of basket
    return easter_basket, basket

# define the main function
def main():
    # prompt the user to enter their name
    name = input("Hi! Who are you?  ") 
    # call the get_list function to get the list of items and the type of basket
    my_list, basket = get_list(name)
    # print the list of items for the easter basket
    print(my_list)
    # print the type of basket chosen by the user
    print(basket)

main()
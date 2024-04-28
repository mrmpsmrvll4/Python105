"""

Programming Assignment: Book Titles Collector

In this assignment, you will create a Python program that collects book titles from a user. 
Your program should use a while loop to prompt the user to enter a total of 10 book titles. 

Follow these steps to complete your assignment:
-----------------------------------------------
1. Set Up the Main Function: Write your program inside a main function. This is where your while loop will be implemented.
2. Collect Book Titles: Use a while loop to ask the customer to enter 10 book titles. Store these titles in a list.
3. Ensure proper capitalization: Use the title function to make sure the first letter is capitalized before storing into the list.
4. Create a Sorted List: Once all titles are collected, save them to a new list named sorted. This list should contain the titles in alphabetical order.
5. Display the Titles: Use a for loop to print each title from the sorted list on a separate line.


"""

# create a program to collect book titles from a user

# function to count books and make a list

def main():
    books = []

    # index
    counter = 0

    # use while loop to repeat for books until there are 10

    while counter <= 10:

        books = addBookToList(books)

        counter+=1

    books.sort()

    print(books)


# make definition to add books to list and make them capitalized
    
def addBookToList(booklist):

    bookInput = input("Please enter 10 book titles: ")

    captdBook = bookInput.capitalize()

    booklist.append(captdBook)

    return booklist


main()

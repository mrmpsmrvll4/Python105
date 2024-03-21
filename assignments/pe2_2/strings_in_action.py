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

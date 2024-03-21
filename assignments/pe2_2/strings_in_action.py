# create a program to collect book titles from a user

#add comments

def main():
    books = []

    counter = 0

    while counter <= 10:

        books = addBookToList(books)

        counter+=1

    books.sort()

    print(books)


    
def addBookToList(booklist):

    bookInput = input("Please enter 10 book titles: ")

    captdBook = bookInput.capitalize()

    booklist.append(captdBook)

    return booklist


main()

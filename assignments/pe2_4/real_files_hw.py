'''

1. Open the file sales_totals in read mode (Download: sales_totals.txt Download sales_totals.txt)
2. Read in all the lines using a loop
3. Strip the newline symbol and convert each line to a float
4. Add each number to the running total
5. Count the number of lines
6. Format and display each number
7. Outside of the loop, format and display the total, the count, and the average
8. Do this using a main function 
9. Use try and except statements to handle file errors

Sample Output:
--------------

13,420.22
45,229.32
...
23,432.32
Total: 547,363.31
Number of entries: 11
Average: 49,760.30

'''

def main():
    try:

        # variable for total sales
        total = 0

        # open the sales file
        accounts = open("sales_totals.txt", 'r')
        
        #read the first line from the file
        line = accounts.readline()

        # loop reading the lines until there aren't any more lines
        while line:

            # read the next line from the file
            line = accounts.readline()

             # Convert the line to a floating-point number and remove any trailing newline character
            line = float(line.rstrip('\n'))

            # print value of the current line to the total
            print(f"\nvalue: {line}")

            # add value of the current line to the total
            total += line

            # print the updated total with commas
            print(f"total: {total:,.2f}")
        # close the file
        accounts.close()

         # Print the last line read from the file (will be an empty string indicating end of file)
        print(line)

    # If an IOError occurs (e.g., file not found or cannot be read), handle the exception
    except IOError:
        print("An IOError has occurred.")


main()

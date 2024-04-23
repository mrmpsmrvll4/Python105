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
        total = 0
        # count
        accounts = open("sales_totals.txt", 'r')
        line = accounts.readline()
        while line:
            line = accounts.readline()
            line = float(line.rstrip('\n'))
            print(f"\nvalue: {line}")
            total += line
            print(f"total: {total:,.2f}")
        accounts.close()
        print(line)

    except IOError:
        print("An IOError has occurred.")


main()

# calculate sales tax

TAX = .05 # tax is a constant, I capitalize constants

def main(): # function
    sales_total = sales() # assigning result of a function to a variable
    sales_tax(sales_total) # passing a variable to a function
    print(f"sales_total: {sales_total}")

def sales_tax(sales_total): # variable becomes parameter
    sales_total = 1000.00
    tax_amt = sales_total * TAX
    print(tax_amt)

def sales():
    my_sales = float(input("What is the price:  "))
    return my_sales

main()
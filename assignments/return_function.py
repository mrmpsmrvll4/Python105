# calculate the interest

def calculate_interest(Principal_Amount, Interest_Rate, Investment_Time):
    result = Principal_Amount * Interest_Rate * Investment_Time /100
    print(result)

result = calculate_interest(1000, 5, 2)
print(f"The simple interest for a principal amount of ${Principal_Amount:,.2f} \
        at an interest rate of {Interest_Rate}% over a period of \
            {Investment_Time} years is: ${calculate_interest:,.2f}")
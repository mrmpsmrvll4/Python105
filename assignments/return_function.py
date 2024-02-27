# calculate the interest

def calculate_interest(Principal_Amount, Interest_Rate, Investment_Time):
    total = (Principal_Amount * Interest_Rate * Investment_Time / 100)
    return total

result = calculate_interest()
print(f"The simple interest for a principal amount of ${Principal_Amount:,.2f} \
                at an interest rate of {Interest_Rate}% over a period of \
                {Investment_Time} years is: ${calculate_interest:,.2f}")

calculate_interest(1000, 5, 2)

#fix so that an answer shows up

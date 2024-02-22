# calculate the interest

def calculate_interest(Principal, Rate, Time):
    total = principal * rate * time /100
    return total

def main():
    result = calculate_interest(principal * rate * time / 100)
    print(f"The simple interest for a principal amount of ${principal_amount:,.2f} \
                at an interest rate of {interest_rate}% over a period of \
                {investment_time} years is: ${calculated_interest:,.2f}")
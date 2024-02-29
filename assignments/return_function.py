# calculate the interest

def calculate_interest(principal_amount, interest_rate, investment_time):
    total = (principal_amount * interest_rate * investment_time / 100)
    return total


def main():
        
    principal_amount = 250000
    interest_rate = 7
    investment_time = 12

    result = calculate_interest(principal_amount, interest_rate, investment_time)
    
    print(f"The simple interest for a principal amount of ${principal_amount:,.2f} ")
    print((f"at an interest rate of {interest_rate}% over a period of {investment_time} years is: ${result:,.2f}"))

        
main()

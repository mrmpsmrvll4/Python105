# Prompting the user to enter the total budget
total_budget = float(input("Enter your total budget: $"))

# Dictionary to store spending categories and amounts
categories = {
        "Housing": 0,
        "Utilities": 0,
        "Groceries": 0,
        "Transportation": 0,
        "Health Care": 0,
        "Personal Care": 0,
        "Clothing": 0,
        "Debt": 0
    }

    # Prompting the user to enter spending amounts for each category
    for category in categories:
        amount = float(input(f"Enter amount spent on {category}: $"))
        categories[category] = amount

    # Calculating the total spent
    total_spent = sum(categories.values())

    # Calculating and displaying the percentage of budget spent on each category
    print("\nBudget Breakdown:")
    for category, amount in categories.items():
        percentage = (amount / total_budget) * 100
        print(f"{category}: ${amount:.2f} ({percentage:.2f}%)")

    # Displaying the total spent and remaining budget
    remaining_budget = total_budget - total_spent
    print(f"\nTotal Spent: ${total_spent:.2f}")
    print(f"Remaining Budget: ${remaining_budget:.2f}")


if __name__ == "__main__":
    main()
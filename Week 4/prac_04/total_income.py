"""
CP1404/CP5632 - Practical 4
Mikhail Bovt
12/10/2025
Calculating a List of Cumulative Totals
"""

def main():
    """Get incomes for a number of months, then show a formatted report."""
    incomes = []
    month_count = int(input("How many months? "))  # renamed from 'months'

    for month in range(1, month_count + 1):
        income = float(input(f"Enter income for month {month}: "))  # f-string 
        incomes.append(income)

    print_income_report(incomes) 


def print_income_report(incomes):
    """Print an income report showing each month's income with total."""
    print("\nIncome Report")
    print("-------------")
    total = 0
    for month_index, income in enumerate(incomes, start=1):
        total += income
        print(f"Month {month_index:2} - Income: ${income:10.2f} Total: ${total:10.2f}")


main()

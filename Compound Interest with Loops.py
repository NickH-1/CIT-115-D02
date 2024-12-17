# Author: Nick Hassett


# Use a while loop to repeat prompting user to input a valid initial deposit.
while True:
    try:  # Use the try statement to catch errors without exiting the program prematurely.
        fltDeposit = float(input("What is the original deposit? (positive number): "))
    except ValueError:  # Handle error-causing string inputs with the except statement, and output an error message.
        print("Please enter a positive numeric value.")
        continue

    if fltDeposit <= 0:
        print("Please enter a positive numeric value.")
    else: break

# Use a while loop to repeat prompting user to input a valid interest rate.
while True:
    try:  # Use the try statement to catch errors without exiting the program prematurely.
        fltMonthlyInterest = float(input("What is the interest rate? (positive number): ")) / 100 / 12
        # Divide by 100 to convert to decimal, then by 12 to get monthly interest.
    except ValueError:  # Handle error-causing string inputs with the except statement, and output an error message.
        print("Please enter a positive numeric value.")
        continue

    if fltMonthlyInterest <= 0:
        print("Please enter a positive numeric value.")
    else: break

# Use a while loop to repeat prompting user to input a valid number of months.
while True:
    try:  # Use the try statement to catch errors without exiting the program prematurely.
        intMonthsCompounded = int(input("How many months? (positive number): "))
    except ValueError:  # Handle error-causing string inputs with the except statement, and output an error message.
        print("Please enter a positive numeric value.")
        continue

    if intMonthsCompounded <= 0:
        print("Please enter a positive numeric value.")
    else: break

# Use a while loop to repeat prompting user to input a valid goal amount.
while True:
    try:  # Use the try statement to catch errors without exiting the program prematurely.
        fltGoalAmount = float(input("What is the goal amount? (enter 0 for no goal, must be positive): "))
    except ValueError:  # Handle error-causing string inputs with the except statement, and output an error message.
        print("Number must be 0 or greater.")
        continue

    if fltGoalAmount < 0:
        print("Number must be 0 or greater.")
    else: break

fltCompoundedDeposit = fltDeposit
# For loop to calculate compound interest in a user-given amount of time
for intMonths in range(1, intMonthsCompounded + 1):
    fltCompoundedDeposit += fltCompoundedDeposit * fltMonthlyInterest
    print(f"Month: {intMonths:>3}\t Account Balance: ${fltCompoundedDeposit:,.2f}")

# Check if there is a goal. If yes, continue and initialize variables to use in a while loop.
if fltGoalAmount > 0:
    fltCompoundedSavings = fltDeposit
    intMonths = 0
    # Start a while loop that checks to see if current savings is less than the user's input goal amount.
    # Increase savings by savings*monthly interest and increment intMonths by 1 every loop to determine how many months are needed.
    while fltCompoundedSavings < fltGoalAmount:
        fltCompoundedSavings += fltCompoundedSavings * fltMonthlyInterest
        intMonths += 1

    print(f"It will take {intMonths} months to reach the goal of ${fltGoalAmount:,.2f}")
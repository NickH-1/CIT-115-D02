# Author: Nick Hassett


# Use a while loop to repeat prompting user to input a valid initial deposit.
fltDeposit = 0
while fltDeposit <= 0:
    try:  # Use the try statement to catch errors without exiting the program prematurely.
        fltDeposit = float(input("What is the original deposit? (positive number): "))
    except ValueError:  # Handle string inputs with the except statement using ValueError, and output an error message.
        print ("Number must be a positive numeric value.")
    else:  # Check once more before repeating the while loop to output an error message for negative values.
        if fltDeposit <= 0: print ("Number must be a positive numeric value.")


# Use a while loop to repeat prompting user to input a valid interest rate.
fltMonthlyInterest = 0
while fltMonthlyInterest <= 0:
    try:  # Use the try statement to catch errors without exiting the program prematurely.
        fltMonthlyInterest = float(input("What is the interest rate? (positive number): ")) / 100 / 12
        # Divide by 100 to convert to decimal, then by 12 to get monthly interest.
    except ValueError:  # Handle string inputs with the except statement using ValueError, and output an error message.
        print ("Number must be a positive numeric value.")
    else:  # Check once more before repeating the while loop to output an error message for negative values.
        if fltMonthlyInterest <= 0: print ("Number must be a positive numeric value.")


# Use a while loop to repeat prompting user to input a valid number of months.
intMonthsCompounded = 0
while intMonthsCompounded <= 0:
    try:  # Use the try statement to catch errors without exiting the program prematurely.
        intMonthsCompounded = int(input("How many months? (positive number): "))
    except ValueError:
        print ("Number must be a positive numeric value.")
    else:  # Check once more before repeating the while loop to output an error message for negative values.
        if intMonthsCompounded <= 0: print ("Number must be a positive numeric value.")


# Use a while loop to repeat prompting user to input a valid goal amount.
fltGoalAmount = -1
while fltGoalAmount < 0:
    try:  # Use the try statement to catch errors without exiting the program prematurely.
        fltGoalAmount = float(input("What is the goal amount? (enter 0 for no goal, must be positive): "))
    except ValueError:
        print ("Number must be 0 or greater.")
    else:  # Check once more before repeating the while loop to output an error message for negative values.
        if fltGoalAmount < 0: print ("Number must be a positive numeric value.")


fltCompoundedDeposit = fltDeposit
# For loop to calculate compound interest in a user-given amount of time
for intMonths in range(1, intMonthsCompounded + 1):
    fltCompoundedDeposit += fltCompoundedDeposit * fltMonthlyInterest
    print(f"Month: {intMonths:>3}\t Account Balance: ${fltCompoundedDeposit:,.2f}")


if fltGoalAmount > 0:  # Check if there is a goal. If yes, continue and initialize variables to use in a while loop.
    fltCompoundedSavings = fltDeposit
    intMonths = 0
    # Start a while loop that checks to see if current savings is less than the user's input goal amount.
    # Increase savings by savings*monthly interest and increment intMonths by 1 every loop to determine how many months are needed.
    while fltCompoundedSavings < fltGoalAmount:
        fltCompoundedSavings += fltCompoundedSavings * fltMonthlyInterest
        intMonths += 1

    print(f"It will take {intMonths} months to reach the goal of ${fltGoalAmount:,.2f}")
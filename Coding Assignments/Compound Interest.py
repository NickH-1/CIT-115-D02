# Author: Nick Hassett


# Prompt user to enter values needed to calculate compound interest.
nPrincipal =    float(input("Enter the starting principal: "))
nInterestRate = float(input("Enter the annual interest rate: "))/100    # Divide by 100 to convert percentage to decimal
nCompounding =  int(input("How many times per year is the interest compounded? "))
nPeriods =      float(input("For how many years will the account earn interest? "))


# Calculate the value with the given inputs and print
print (f"At the end of {nPeriods:g} years you will have $ {nPrincipal * ((1 + (nInterestRate / nCompounding)) ** (nCompounding * nPeriods)):,.2f}")
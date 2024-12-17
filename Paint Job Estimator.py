# Author: Nick Hassett

import math

# This program calculates the cost of getting a wall painted, and writes it to a file!!
def main():

    # Call the getFloatInput function and pass in a prompt string for each variable
    fltWallSquareFeet       = getFloatInput("Enter the wall space in square feet: ")
    fltPaintPrice           = getFloatInput("Enter the price of paint per gallon: ")
    fltFeetPerGallon        = getFloatInput("Enter feet per gallon: ")
    fltLaborHoursPerGallon  = getFloatInput("Enter labor hours per gallon: ")
    fltLaborChargePerHour   = getFloatInput("Enter labor charge per hour: ")

    # Get state to determine tax rate later
    strState =    input("State the job is in: ")

    # Ask for customer's last name to use in filename
    strLastName = input("Customer's last name: ")

    # Math out values that are needed for other functions, with some functions. Getting funcy.
    intGallonsRequired = getGallonsOfPaint(fltWallSquareFeet, fltFeetPerGallon)
    fltLaborHours      = getLaborHours(fltLaborHoursPerGallon, intGallonsRequired)

    # Calculate and store values that will pass into the final function
    fltLaborCost      = getLaborCost(fltLaborHours, fltLaborChargePerHour)
    fltPaintTotalCost = getPaintCost(intGallonsRequired, fltPaintPrice)
    fltStateTax       = getSalesTax(strState)

    # Pass the final values in to display the calculations and return a string to be used to write to file
    strFileOutput = showCostEstimate(fltPaintTotalCost, fltLaborCost, fltStateTax)

    # Create a variable and store a string with the user's input last name to be used for file naming
    paintJobFile = f"{strLastName}_PaintJobOutput.txt"

    # Open file in write mode, write to file, and then close file.
    outputFile = open(paintJobFile, "w")
    outputFile.write(strFileOutput)
    outputFile.close()

    # Notify the user that the file was created.
    print (f"File: {paintJobFile} was created.")


# Pass in a string to prompt for a positive number entry, and validate
# Loops until a valid input is entered
def getFloatInput(strInputPrompt):
    while True:
        try:
            userInput = float(input(strInputPrompt))
        except ValueError:
            print("You must enter a number.")
        else:
            if userInput > 0:
                break
            else:
                print("You must enter a number that is greater than zero.")

    return userInput

# Does some math and returns the result
def getGallonsOfPaint(wallArea, feetPerGallon):
    return math.ceil(wallArea / feetPerGallon)

# Does some math and returns the result
def getLaborHours(hoursPerGallon, totalGallons):
    return hoursPerGallon * totalGallons

# Does some math and returns the result
def getLaborCost(laborHours, costPerHour):
    return laborHours * costPerHour

# Does some math and returns the result
def getPaintCost(gallons, price):
    return gallons * price

# Use passed string to determine state tax. If not matching, output 0.
def getSalesTax(state):
    if state == "CT" or state == "VT":
        tax = 0.06
    elif state == "MA":
        tax = 0.0625
    elif state == "RI":
        tax = 0.07
    elif state == "ME":
        tax = 0.085
    else:
        tax = 0
    return tax

# Function that will return the final calculations as a formatted string
def showCostEstimate(paintCost, laborCost, taxRate):
    taxTotal = (paintCost + laborCost) * taxRate
    fullTotal = paintCost + laborCost + taxTotal

    outputText = str(f"Paint charges: ${paintCost:,.2f}\n"
                     f"Labor charges: ${laborCost:,.2f}\n"
                     f"Tax: ${taxTotal:,.2f}\n"
                     f"Total: ${fullTotal:,.2f}")

    print(outputText)
    return outputText

if __name__ == "__main__":
    main()

# Author: Nick Hassett

# getFloatInput function is passed a prompt string,
# and a numerical value that determines the lowest number allowed.
# Takes user input and converts it to a float.
# Repeats the request if the input would throw an error,
# or if the input is under the desired value.
def getFloatInput(strInputPrompt, minValue):
    while True:
        try:
            userInput = float(input(strInputPrompt))
            if userInput <= minValue:
                raise ValueError
            break
        except ValueError:
            print(f"You must enter a positive number over {minValue}.")

    return userInput

# getMedian function is passed a list, which is then checked with modulus division
# to determine if the number of elements is even or odd.
# If odd, assigns the middle element in the list to medianOfList,
# determined by dividing the list's size in half with integer division.
# If even, obtains the two middle elements in the same way, adds them together,
# and divides by 2 to average.
def getMedian(inputValues):
    size = len(inputValues)
    if size % 2 == 1:
        medianOfList = inputValues[size//2]
    else:
        medianOfList = (inputValues[size//2] + inputValues[(size//2)-1]) / 2

    return medianOfList


def main():

    # Initialize a list in preparation for user input.
    salesValues = []

    # Initialize variable primed with string "Y" to start the while loop.
    keepGoing = "Y"

    # Obtain sales values by calling the getFloatInput to ask for, and validate inputs.
    # Append valid inputs to the list initialized previously, and ask the user to enter
    # either the character "Y" or "N", and repeats the request until one of the desired values
    # is entered.
    while keepGoing == "Y":
        fltSalesValue = getFloatInput("Enter property sales value: ", 0)
        salesValues.append(fltSalesValue)
        keepGoing = input("Enter another value? Y or N: ").upper()
        while keepGoing != "Y" and keepGoing != "N":
            keepGoing = input("Enter Y or N: ").upper()

    # Sort the list.
    salesValues.sort()

    # Whole bunch of math here
    smallestSale = min(salesValues)
    largestSale = max(salesValues)
    medianSale = getMedian(salesValues)
    totalSales = sum(salesValues)
    averageSale = totalSales/len(salesValues)
    commission = totalSales * .03

    # Prime a variable to use for numbering list outputs.
    propertyNumber = 1

    # Format and print the elements in the list with a for loop.
    # Increment the propertyNumber variable after it is printed.
    for num in salesValues:
        print(f"Property {propertyNumber}:     ${num:>12,.2f}")
        propertyNumber += 1

    # Format and print out the rest of the variables.
    print(f"\nMinimum:        ${smallestSale:>12,.2f}\n"
            f"Maximum:        ${largestSale:>12,.2f}\n"
            f"Total:          ${totalSales:>12,.2f}\n"
            f"Average:        ${averageSale:>12,.2f}\n"
            f"Median:         ${medianSale:>12,.2f}\n"
            f"Commission:     ${commission:>12,.2f}\n")


if __name__ == "__main__":
    main()
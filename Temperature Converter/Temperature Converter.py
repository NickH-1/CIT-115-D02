# Author: Nick Hassett

print("Nick's Temp Converter:\n")

# Prompt user for inputs
nTemperature = float(input("Enter a temperature: "))
sTempType = input("Is the temp F for Fahrenheit or C for Celsius? ").upper()  # Convert input to uppercase to catch valid letters that were entered as lowercase

if sTempType == "F" or sTempType == "C":  # Continue if temp type was valid

    # Use shortcut if statements for fun and to limit number of lines of repetitive code
    nTempLimit = 212 if sTempType == "F" else 100
    sConvertType = "Celsius" if sTempType == "F" else "Fahrenheit"
    nConvertedTemp = (5.0 / 9) * (nTemperature - 32) if sTempType == "F" else ((9.0 / 5.0) * nTemperature) + 32

    if nTemperature > nTempLimit:  # Compare user's temp to max temp
        print(f"Temp can not be > {nTempLimit}.")
    else:
        print(f"The {sConvertType} equivalent is: {nConvertedTemp:.1f}")

else:
    print("Please enter F or C.")  # Exit if invalid string input

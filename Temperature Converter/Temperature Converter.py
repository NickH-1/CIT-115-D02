# Author: Nick Hassett

print("Nick's Temp Converter:\n")

# Prompt user for inputs
nTemperature = float(input("Enter a temperature: "))
sTempType = input("Is the temp F for Fahrenheit or C for Celsius? ").upper()  # Convert input to uppercase to catch valid letters that were entered as lowercase

if sTempType == "F" or sTempType == "C":  # Continue if temp type was valid

    if nTemperature > (212 if sTempType == "F" else 100):  # Compare user's temp to max temp and continue to conversion if under
        print(f"Temp can not be > {212 if sTempType == "F" else 100}.")
    else:
        print(f"The {"Celsius" if sTempType == "F" else "Fahrenheit"} equivalent is: "
              f"{(5.0 / 9) * (nTemperature - 32) if sTempType == "F" else ((9.0 / 5.0) * nTemperature) + 32:.1f}")  # Output formatted and converted temperature

else:
    print("You must enter F or C.")  # Exit if invalid string input
# Author: Nick Hassett

sName = input("Name of person whose grades are being calculated: ")


iTest1 = int(input("Test 1: "))
iLowestGrade = iTest1  # Initialize a variable for the lowest grade with the first input.

iTest2 = int(input("Test 2: "))
if iTest2 < iLowestGrade: iLowestGrade = iTest2  # Compare the new input to the lowest recorded grade and change it if true.

iTest3 = int(input("Test 3: "))
if iTest3 < iLowestGrade: iLowestGrade = iTest3  # Compare the new input to the lowest recorded grade and change it if true.

iTest4 = int(input("Test 4: "))
if iTest4 < iLowestGrade: iLowestGrade = iTest4  # Compare the new input to the lowest recorded grade and change it if true.


if iTest1 < 0 or iTest2 < 0 or iTest3 < 0 or iTest4 < 0:  # Check if any entered numbers are less than 0.
    exit(print("Test scores must be greater than 0."))


sDropLowest = input("Do you wish to drop the lowest grade? (Y or N): ")
if sDropLowest != "Y" and sDropLowest != "N":  # Exit the program if the input is invalid.
    exit(print("Enter Y to drop the lowest grade or N to calculate all grades."))

# Utilize a shorthand if statement to do the math based on user's input to drop the lowest grade.
fTestAvg = (iTest1 + iTest2 + iTest3 + iTest4 - iLowestGrade)/3 if sDropLowest == "Y" else (iTest1 + iTest2 + iTest3 + iTest4)/4

#  Compare avg test score to numbers to determine a letter grade. Cheeky line reduction with shorthand if statements.
#  Not sure which is worse, horizontal or vertical bloat. Honestly, I like this way better. Feels more categorized.
#  3 values in the shorthand if statement definitely feels like I'm pushing it, though.
if fTestAvg >= 90:
    sLetterGrade = "A+" if fTestAvg >= 97 else "A" if fTestAvg >= 94 else "A-"
elif fTestAvg >= 80:
    sLetterGrade = "B+" if fTestAvg >= 87 else "B" if fTestAvg >= 84 else "B-"
elif fTestAvg >= 70:
    sLetterGrade = "C+" if fTestAvg >= 77 else "C" if fTestAvg >= 74 else "C-"
elif fTestAvg >= 60:
    sLetterGrade = "D+" if fTestAvg >= 67 else "D" if fTestAvg >= 64 else "D-"
else:
    sLetterGrade = "F"


print (f"{sName} test average is: {fTestAvg:.1f}\n"
       f"Letter grade for the test is: {sLetterGrade}")
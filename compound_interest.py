# Coding Challenge 1, compound_interest.py
# Name: Tejvir Sohi
# Student No: 1926434

# Compound Interest Calculator

"""
Requirements:
    You will develop a program to calculate compound interest.

    • Print a welcome message explaining the purpose of the program.
    • Prompt the user for the necessary inputs (see formulae and brief)
    • Convert input values to suitable data types.
    • Perform compound interest calculation using the forumlae provided.
    • Print the result to the terminal using appropriate formatting.
    
    • Your program should be as close as possible to the example shown in the assessment brief.

Constraints:
    • Ensure that the interest rate is entered as a percentage and not a decimal.
    • Ensure that all monetary values are formatted to two decimal places.

Hints:
    • Think about what data types are the most appropriate for each input value.
    • Order of operations will be important, make sure you use parenthesis.
    • Review lecture two for more information on string formatting.
    • Your programs output should be as close as possible to the example in the assessment brief.
"""

# TODO: Write your code here!
# This first print statement welcomes the user to the compound interest calculator

print(""" Welcome to the Compound Interest program.
The purpose of this program is to calculate compound interest for you""")
'''
The set of of input statements take in the required inputs from the user.
They are also stored in appropriatley named variables
'''
principalAmount = int(input("Please enter in the amount of money you are starting with: "))
rateOfInterest = float(input("Please enter the rate of interest: "))
noOfInvestYears = int(input("Please enter the number of years the amount is invested for: "))
print('''Please enter the number of times you are compounding in a year:
Enter 1 for Annually
Enter 12 for Monthly
Enter 6 for Half-Yearly
Enter 4 for Quarterly  ''')
compIntPerYear = int(input("Please enter your choice here: "))

# The 2 print statments below print the initial headers
print(f"Year\tStarting Balance\tInterest\tEndingBalance")
print("-"*60)


# The variable declarations and initialisations are done below to be used in the while loop
totalPeriods = compIntPerYear * noOfInvestYears
period = 1
yearCount = 1
startingBalance = principalAmount

# A while loop is initialised while the value of period is less than or equal to total periods
while period <= totalPeriods:
    year = ""
    '''The if statement below checks if the periof minus 1 divded by the number of times the interest is compounded in a year has a remainder of 0
    if the statement evaluates to true, the value of year count is stored as a string in the variable year and yearCount is incremented by 1'''
    if (period - 1) % compIntPerYear == 0:
        year = str(yearCount)
        yearCount += 1
    # Caluations are done below for the values that will be displayed. They are then outputted to the user and values are incremented.
    endingBalance = startingBalance * (1 + (rateOfInterest / 100) / compIntPerYear)
    interest = endingBalance - startingBalance
    print('{0:<8} {1:<10} {2:<15} {3:<12} {4:<15}'.format(year, period, "{0:.2f}".format(startingBalance), "{0:.2f}".format(interest), "{0:.2f}".format(endingBalance)))
    startingBalance = endingBalance
    period += 1

# The final amount at the end of the year is calculated here
amount = float("{0:.2f}".format(principalAmount * (1 + (rateOfInterest / 100) / compIntPerYear) ** (compIntPerYear * noOfInvestYears)))
# The result is then outputted here
print(f"\n£{principalAmount} invested at {rateOfInterest}% for {noOfInvestYears} years compounded {compIntPerYear} times per year is: £{amount}")

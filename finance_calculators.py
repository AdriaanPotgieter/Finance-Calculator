'''
Compulsory task
This program will allow the user to choose which type of calculator they want to use and then the program will
do calculations for the user.
'''
# I will import math as there will be complicated calculations to be made.
import math

# Ask the user to enter investment or bond and describe the difference between the two.
choice_of_calculator = input(f"""Choose either 'investment' or 'bond' from the menu below to proceed: \n
investment - to calculate the amount of interest you'll earn on interest
bond - to calculate the amount you'll have to pay on a home loan.
""").capitalize()

if choice_of_calculator == "Investment" :
# Asking user to enter the amount they want to invest ans store it as a float.
    amount1 = float(input("Enter the amount of money you are depositng:\n"))
# Asking user the interest rate. They will enter the number only and storing it as a float.
    interest_rate1 = float(input("Enter the interest rate here. The number only:\n"))
# Asking user to enter how long they want to invest it for.
    total_years = int(input("Enter the number of years that you would like to invest for:\n"))
# Asking user if they want compound interest or simple interest.
    interest = input("Would you like compound interest or simple interest? (Enter compound or simple):\n").capitalize()

# Created a new variable so that the value can work in the calculation and is correct according to formula.
    interest_rate2 = interest_rate1 / 100
# If user selected 'compound' this statement will print. The formula for compound interest is: A = P(1 +r)^t. 
    if interest == "Compound":
# Created a new variable to round off the number to two decimals and makes it easier to add to a sentence.
        compound_total = round(amount1*math.pow((1 + interest_rate2), total_years), 2)
        print("This will be your total R", compound_total)
# If user selected 'simple' this statement will print. The formula for simple interest is : A = P(1 + r x t).
    if interest == "Simple" :
# Created a new variable to round off the value to two decimals and makes it easier to add to a sentence.
        simple_total = round(amount1*(1 + interest_rate2*total_years), 2)
        print("This will be your total R", simple_total)

# If user selected 'bond' then this statement will execute.
elif choice_of_calculator == "Bond" :
# Will ask user to enter the present value of their house.
    present_value_house = float(input("Enter the present value of your house:\n"))
# Will ask them to enter the interest rate here.
    interest_rate3 = float(input("Enter the interest rate here:\n"))
# Will ask the user to enter the total number of months they plan to take to repay the bond. 
    num_of_months = int(input("Enter the number of months you plan to take to repay the bond:\n"))
# I will calculate the interest rate so that it can be used in the equation and round it off to two decimals.
    interest_rate4 = interest_rate3/ 100 / 12
# Created a new variable to round off the value to two decimals and makes it easier to add to a sentence.
    repayment = round((interest_rate4 * present_value_house) / (1 - (1 + interest_rate4)**(- num_of_months)), 2)
    print("This will be your monthly repayment: R ", repayment)

# This statement will print if the user did not enter investment or bond.
else:
    print("Your entery is incorrect. Please enter investment or bond")       
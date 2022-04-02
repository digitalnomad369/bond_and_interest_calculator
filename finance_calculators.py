

# PROGRAM THAT ALLOWS USER TO ACCESS TWO DIFFERENT FINANCIAL CALCULATORS


import math    # imports math module function




# ========== A. USER SELECTION ==========

'''
The user is asked to select either investment or bond in order to
access the financial calculator relevant to their selection.

A brief explanation of each possible option is also displayed to the user.
'''


fin_calc = input('''\nChoose either 'investment' or 'bond' from the menu below to proceed:

investment  - to calculate the amount of interest you'll earn on an investment
bond        - to calculate the amount you'll have to pay on a home loan

''')




# ========== B. INVESTMENT CALCULATION ==========

# if user selected "investment" the following questions will be asked:

'''
A nested IF STATEMENT is added below to calculate the user's chosen
interest option (simple or compound) on their investment.
'''


if fin_calc.lower() == "investment":
    
    invest_amount = float(input("\nEnter the amount of money you are investing: "))
    
    interest_rate = float(input("\nEnter the interest rate.(Enter only the number of the interest rate): "))
    
    time = int(input("\nEnter the number of years you intend to invest the money for: "))
    
    interest = input('''\nWhat type of interest do you want on your investment?
(simple or compound): ''')
    
    interest_rate = interest_rate/100
    
    if interest.lower() == "simple":
        
        total_amount = round(invest_amount * (1+ interest_rate * time))    
        
        print(f'''\nYour final investment amount after {time} years at simple interest rate is
R{total_amount}.''')

        # user's final investment amount after chosen period at simple interest rate is displayed
        
    else:
        
        total_amount = round(invest_amount * math.pow((1 + interest_rate), time))  
        
        print(f'''\nYour final investment amount after {time} years at compounded interest rate is
R{total_amount}.''')
        
        # user's final investment after chosen period at compounded interest rate is displayed



        
# ========== C. MONTHLY BOND REPAYMENT CALCULATION ==========


# else if user selected "bond", the following questions will be asked:

elif fin_calc.lower() == "bond":
    
    value_of_house = float(input("\nEnter the present value of the house you wish to purchase: "))
    
    interest_rate= float(input("\nEnter the interest rate.(Enter only the number of the interest rate): "))
    
    num_of_months = int(input("\nEnter the number of months you intend to repay the bond for: "))
    
    interest_rate = interest_rate/100
    
    monthly_repay = round((interest_rate/12 * value_of_house)/(1 - (1+interest_rate/12)**(-num_of_months)))
    
    print(f"\nYour monthly repayments on selected bond is R{monthly_repay}.")

    # user's monthly bond repayments is displayed


# if user made an invalid entry, they will get the following error message:

else:
    print("\nERROR! You have made an invalid selection. Program is unable to proceed.")


# END PROGRAM




    
    
    

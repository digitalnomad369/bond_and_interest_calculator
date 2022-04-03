# Capstone Project I - Variables and Control Structures #

# TABLE OF CONTENTS #

[Purpose of project](#Purpose-of-project)

[Requirements](#Requirements)

[Packages](#Packages)

[Application components](#Application-components)

[Contributors](#Contributors)

[License and copyright](#License-and-copyright)

# Purpose of project #

The purpose of this Capstone Project is to showcase my programming skills in handling variables and control structures in Python. It also forms part of my developer
portfolio.

In this Capstone Project, I designed a finance calculator application that enables a user to either calculate their interest on an investment or monthly bond repayments.

# Requirements #

In  order to *run and test* this program, you require the following:
- Python v3.7 or higher installed 
  - To download Python click the following link: *https://www.python.org/downloads/*

# Packages #

Python's __math module__ is imported to access and perform additional mathematical operations in the application. 

# Application components #
Open and run __finance_calculators.py
This application comprises the following 3 sections: 
##### 1. USER MENU:
      - This is the screen that the user will be see when they open the application. 
      - The user will be prompted to select one of two options: "investment" OR "bond" 
      ![user_menu](https://user-images.githubusercontent.com/102178512/161421745-b7da42e2-a4a7-4b38-a2bd-144c96e70e82.jpg)
      
##### 2. INVESTMENT CALCULATOR:
      - If user opted for the investment calculator, they will be asked to enter the principal investment amount, interest rate(divided by 100, time and 
        type of interest (simple or compound) they want on their investment. 
        
      - Simple interest calculation:
        - total_amount = round(invest_amount * (1+ interest_rate * time))
        
      - Compound interest calculation:
        - total_amount = round(invest_amount * math.pow((1 + interest_rate), time)
      ![investment_calculators](https://user-images.githubusercontent.com/102178512/161421960-890d1029-a2b8-4e44-881f-f644e659968c.jpg)

##### 3. BOND REPAYMENT CALCULATOR:
      - If user selected "bond", they will be redirected to the bond repayment calculator. 
      - In order to calculate the user's monthly bond repayments, the user will be prompted to enter the value of the property they are purchasing, 
        the interest rate(divided by 100) and the number of months in which they intend to repay the bond. 
        
      - Bond repayment calculation:
        - monthly_repay = round((interest_rate/12 * value_of_house)/(1 - (1+interest_rate/12)**(-num_of_months)))
        ![bond_repayment_calculator](https://user-images.githubusercontent.com/102178512/161422249-0b55594b-2fcf-415c-bea8-b6a61bfc8734.jpg)
        
# Sample output of application
![investment_simple_interest](https://user-images.githubusercontent.com/102178512/161422493-59e24231-eba4-43c8-9e6c-e9271e1fa63e.jpg)
![bond_repayment](https://user-images.githubusercontent.com/102178512/161422499-9bea6b85-7688-4833-b33f-4306cd3cd559.jpg)

# Contributors
- Tammy-Lee Bastian tammyleebastian@gmail.com

# License and copyright
(c) Tammy-Lee Bastian, HyperionDev
Licensed under the [MIT License](LICENSE)


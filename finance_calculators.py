#The programme asks the user to enter either investment or bond 
#If the user selects investment then they can either enter simple or compund 
#They can then enter the amount they want to deposit, the interest rate, and the duration of their investment in years 
#The value of their investment after the chosen duration will appear as an output 
#If the user chooses bond then the ouput will be the monthly repayment of the bond considering interest rate, repayment plan, and the value of the bond

import math 

print('Investment - to calculate the amount of interest you\'ll earn on your investment')
print('Bond - to calculate the amount you\'ll have to pay on a home loan')

type = input('Enter either \'investment\' or \'bond\' from the menu above to proceed. ')

if type == 'investment' or type == 'Investment' or type == 'INVESTMENT': 
    deposit = float(input('Enter the amount of money you are depositing: '))
    interest_rate = float(input('Enter the interest rate as a percentage: '))
    duration = int(input('Enter the number of years you are palnning to invest: '))
    interest = input('Do you want \"simple\" or \"compound\" interest? ')

    if interest == 'simple' or interest == 'Simple' or interest == 'SIMPLE': 
        print(deposit*(1+10*(interest_rate/100)))
    if interest == 'compound' or interest == 'Compound' or interest == 'COMPOUND': 
        print((deposit*(1+(interest_rate/100)))**duration)

if type == 'bond' or type == 'Bond' or type == 'BOND': 
    house_value = float(input('Enter the present value of the house: ')) 
    int_rate = float(input('Enter the interest rate: '))
    repayment_time = 'Enter the number of months you plan to take to repay the bond: '
    monthly_int = (int_rate/100)/12
    repayment_value = (monthly_int*house_value)/(1-((1+monthly_int)**(repayment_time*(-1))))
    print(repayment_value)


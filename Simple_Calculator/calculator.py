# This programme codes for a simple calculator. 
# The user can either choose to perform an operation between two numbers 
# or display all the calculations done with equations with their results. 


# This piece of code creates a text file to store the eqautions with their 
# solutions if there is not one
import os

if not os.path.exists("equations.txt"):
    with open("equations.txt", "w") as file:
        pass


# This function codes for the caclulator and 
# stores the equations with their results to the text file
def calculation():
    print('''
Enter two numbers and an operator that you want to perform on those numbers.
Valid operators: 
    + = addition 
    - = substraction 
    * = multiplication 
    / = division 
    % = modulo 
    
    ''')

    while True: 
        try: 
            num1 = float(input('Number 1: '))
            break     
        except ValueError: 
            print('Oops! That was not a valid number. Try again...')

    operators = ['+', '-', '*', '/', '%']
    operator = input('Operator: ')


    if operator not in operators: 
        raise Exception('Not valid operator. Try again...')


    while True: 
        try: 
            num2 = float(input('Number 2: '))
            break
        except ValueError: 
            print('Oops! That was not a valid number. Try again...')


    if operator == '+':
        result = num1 + num2
        print(result)

    elif operator == '-':
        result = num1 - num2
        print(result)

    elif operator == '*':
        result = num1 * num2
        print(result)
    
    elif operator == '%':
        result = num1 % num2
        print(result)

    if operator == '/':
        while True:
            try:
                res = num1 / num2
                print(res)
                break
            except ZeroDivisionError:
                print('Cannot divide by 0.')
                break

    with open('equations.txt', 'a') as file: 
        if num2 != 0 and operator != '/':
            file.write(f'{num1} {operator} {num2} = {result}. \n')

        if num2 == 0 and operator == '/':
            file.write(f'{num1} {operator} {num2} (Cannot divide by 0!) \n')
    file.close()


# This function dispalys the equations with their results on the screen
def display(): 
    with open('equations.txt', 'r') as file: 
        print(file.read())
    file.close()
    

# The user can choose to recall either of the previous two functions
options = ['c', 'equations']

print('To perform a calculation input \'C\', to dispaly all the previous calculations input \'equations\'.\n')

user_choice = str(input('Enter your choice: ')).lower()
if user_choice not in options: 
    raise Exception('Your choice is not one of the exceptions. Please try again...')       

if user_choice not in options:
    raise Exception('Please enter a valid option.')

if user_choice == 'c': 
    print(calculation()) 

if user_choice != 'c':
    if user_choice == 'equations': 
        print(display())
                

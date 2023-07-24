#Ask the user to input the year they were born
#Ask the user to input their last birthday year 
#Calculate the age of the user by taking away 
# the last birthday year of the user 
# from the year of birth of the user 
#If the result is 18 or more output Congrats, you are old enough

user_bday = int(input('Please enter the year you were born in: '))
last_bday = int(input('Please enter your last birthday\'s year: '))

age = last_bday - user_bday

if age>= 18: 
    print('Congrats, you are old enough.')
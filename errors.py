print("Welcome to the error program")  #Syntax error: missing brackets
print("\n") #Sytax error: missing brackets and incorrect indentation

age = input('How old are you? ')    #Runtime error: double equal signs to assign a value to a variable, syntax error incorrect indentation, logical error: only need the age not a sentence
#Runtime error: cannot convert a sentence to an integer, logical error: it is not necessary to convert age into an integer at this point
print("I\'m " + age + " years old.")       #Syntax error: there should be empty spaces separate the age from the other words, and a backslash to escape the reverse quotation mark        


answerYears = int(age) + 3   #Logical error 
print("The total number of years: " + str(answerYears) + '.') #Syntax error: missing brackets, logical error: name of variables in brackets, no full stop
answerMonths = 6 + (answerYears * 12)   #Logical error
print("In 3 years and 6 months, I\'ll be " + str(answerMonths) + " months old.") #Runtime error: cannot concatenate an integer with a string, syntax error: missing brackets, logical error: no full stop

#HINT, 330 months is the correct answer
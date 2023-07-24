#This programme asks the user to always input a number 
#If the user enters -1 then the programme will no longer asks the user to input a number 
#The programme then outputs the average of the inputs except -1

sum = 0
counter = 0
while True: 
    num = float(input('Please enter a number: '))
    if num == -1: 
        break
    counter += 1   
    sum += num

average = sum/counter
print(round(average, 2))
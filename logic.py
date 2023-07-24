#Calculating the average of any 5 numbers
sum = 0
counter = 0
while True: 
    num = float(input('Please enter a number: '))
    counter += 1   
    sum += num
    if counter > 5: 
        break 

average = sum/counter
print(round(average, 2))
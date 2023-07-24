#This programme asks the user to input the names of all the pupils in a class one by one 
#If the user inputs 'stop' the loop breaks and outputs the number of names entered 

print('Enter the names of all the pupils in the class one at a time.')
print('Enter \"stop\" when you have finished to enter all the names.')
print()
counter = 0
while True: 
    names = input('Enter names: ')
    if names == 'stop' or names == 'Stop' or names == 'STOP': 
        break 
    counter += 1

print(counter)
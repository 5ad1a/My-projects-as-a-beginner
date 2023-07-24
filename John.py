#This programme asks the user to input a name, until they enter 'John', and it outputs a list of all the name entered before the name 'John'

list_incorrect_names = []

while True: 
    name = (input('Enter you name: ')).capitalize()
    if name == 'John':
        break 
    list_incorrect_names.append(name)
print(list_incorrect_names)
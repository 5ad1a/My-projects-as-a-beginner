"""
This programme reads the file DOB.txt where the names and birthdates of each person 
are written on a single sentence and different sentences are separated by a coma
and outputs the text in the format 

Name
Orville Wright
Rogelio Holloway
Marjorie Figueroa
…etc

Birthdate
21 July 1988
13 September 1988
9 October 1988
…etc

""" 

file = open('DOB.txt', 'r')

l = file.readline()

list = l.split(',')
del list[-1]

new_list = []
x = 0
for x in range(len(list)):
    new_list.append(list[x].split(' '))
    x += 1

y = 0
print('Name')
for y in range(len(list)): 
    print(f'{new_list[y][0]} {new_list[y][1]}')

y = 0
print('\n\nBirthdate')
for y in range(len(list)): 
    print(f'{new_list[y][2]} {new_list[y][3]} {new_list[y][4]}') 



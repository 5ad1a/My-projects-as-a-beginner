"""This programme reads a Text File in the form 
- Min: 1,2,3,5,6 
- Max: 1,2,3,5,6
- Avg: 1,2,3,5,6 

and returns it in the form 
- The min of [1, 2, 3, 5, 6] is 1
- The max of [1, 2, 3, 5, 6] is 6
- The avg of [1, 2, 3, 5, 6] is 3.4

The only operations are min, max, and avg
The programme can handle any combination of operations and any length of input numbers
The list should not be empty and should contain valid integers
"""

import math

# this opens the file input.txt for reading only
# each line in the file is read as a list with one item
# the last character of each line except the last line is a newline 
file = open('input2.txt', 'r')
lines = file.readlines()


for line in lines: 
    # for each line (now lists) the first 5 characters are removed, and we are left with numbers separated by commas
    new_lines = line.strip(line[0:5]) 

    # the numbers are stored into a list as strings
    list_num_str = new_lines.split(',')
    print(list_num_str)

    # we remove the string with a space only
    list_num_str[-1] = list_num_str[-1].strip()


# a new list is created and the numbers from the prevous lists are stored as integers
list_num_int = []

i = 0
for i in range(len(list_num_str)):
    list_num_int.append(int(list_num_str[i]))
    i += 1


# a functions that outputs the maximum value from the corrisponding list of integers
def max_num(): 
    if line[:3] == 'max':
        return max(list_num_int)


# a functions that outputs the minimum value from the corrisponding list of integers
def min_num(): 
    if line[:3] == 'min':
        return min(list_num_int)


# a functions that outputs the average of the corrisponding list of integers        
def average(): 
    if line[:3] == 'avg':
        return round(sum(list_num_int)/len(list_num_int), 2)


# open a new file output.txt and write the output of each function in an appropriate sentence
file_2 = open('output2.txt', 'w') 

for line in lines:  
    file_2.write(f'The min of {str(list_num_int)} is {min_num()}.\n')
    file_2.write(f'The max of {str(list_num_int)} is {max_num()}.\n')
    file_2.write(f'The avg of {str(list_num_int)} is {average()}.\n')

file.close()
file_2.close()
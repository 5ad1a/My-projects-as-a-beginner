""""This programme asks the user to input ten numbers (integers or decimals), 
it stores those ten numbers in a list, 
it then outputs the sum of all the numbers, the indexes of the maximum and the minumum, 
calculates the average and outputs it up to two decimal places, 
find the median number and outputs the result
"""

import math 

num_list = []

print('You need to enter ten numbers, that can be either whole numbers or decimals.\n')

x = 0

for x in range(10):
    num = float(input('Enter number: '))
    num_list.append(num)
    x += 1

sum_list= sum(num_list)
print('The sum is ' + str(sum_list))

print('The index of the maximum number is '+ str(num_list.index(max(num_list))))

print('The index of the minimum number is '+ str(num_list.index(min(num_list))))

print('The average is ' + str(round(sum_list/10, 2)))

num_sorted = sorted(num_list)
print('The median is '+ str(round(((num_sorted[4]+num_sorted[5])/2), 2)))
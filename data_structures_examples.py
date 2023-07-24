a = [1, 2, 3]
b = [4, 5, 6]
c = [a, b, 7, 8, 9]    #in this case a and b are nested lists

""""**************************************************************************************************************************************************"""
gh = c 
print(gh)    #prints [[1, 2, 3], [4, 5, 6], 7, 8, 9]

print(c)   #prints [[1, 2, 3], [4, 5, 6], 7, 8, 9]

c.remove(b)
print(c)    #prints [[1, 2, 3], 7, 8, 9]

""""*************************************************************************************************************************************************"""

d = a[:]        #[:] is a slice operator, in this case copying the entire list, but can be used to copy only a portion of a list too
print(d)   #prints [1, 2, 3]

d[1] = 10
print(a)     #prints [1, 2, 3] -> a remains unchanged because d is referencing to a and not vice versa, this is called shallow copying
print(d)    #prints [1, 10, 3] -> d refers to the original version of a

a[0] = 20 
g = a[:]
print(g)    #prints [20, 2, 3]

""""-------------------------------------------------------------------------------------------------------------------------------------------------"""
b[0] = 'n'
e = b
b[0] = 40 
print(e)     #prints [40, 5, 6]

f = b 
f[0] = 50 
print(b)     #prints [50, 5, 6]

j = c 
c[0] = 0
print(j)   #prints [0, 7, 8, 9]

""""***************************************************************************************************************************************************"""

num = [12, 13, 14, 15, 16, 17]
print(num[0]+1)
num_ints = [int(i) for i in num]
print(num_ints[0]+1)

""""***************************************************************************************************************************************************"""

'''copy() method ensures that if you modify the copied list the original list stays the same 
If the original list contains other lists as items those inner lists can still be modified
if the corrisponding copied list is modified
The copy.copy() method makes a shallow copy as slicing does
deepcopy() makes a copy of the list and any list contained in it
need to import the copy module as 'import copy' to ise the copy() and deepcopy() methods''' 

import copy
a = [[1,2,3], [4, 5, 6]]
b = a[:]
c = copy.deepcopy(a) 

b[0][1] = 10 # changes position [0][1] in both b and a
c[1][1] =12

print(a) # prints [[1, 10, 3], [4, 5, 6]]
print(b) # prints [[1, 10, 3], [4, 5, 6]]
print(c)
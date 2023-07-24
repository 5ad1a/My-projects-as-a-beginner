l = [1, 2, 3, 4, 5]

def max_num(list): 
    list = l
    return max(list)

def min_num(list): 
    list = l
    return min(list)

d = {8: 'eight', 8: 'red'}

l.append(d)

d[9] = 'nine'


li = [{1: 'one', 2: 'two'}, {1: 'eleven', 2: 'twelve'}, {1: 'one', 2: 'four'}, {1: 'one', 2: 'six'}]

g = {1: 'a', 2: 'b', 3: 'c', 4: 'a', 5: 'a', 6: 'f'}

dl = list(g.keys())

'''r = 0
for r in range(len(dl)): 
    if g[dl[r]] == 'a': 
        print('y')'''

'''n = 0
z = 1
for n in range(len(li)):
    if li[n][1] == 'one': 
        n += 1
        print('t ' + str(z))
        z += 1
print(z-1)'''

dict = {'pilot': 'airplane', 'nurse': 'hospital'}

from datetime import datetime, date 
date_format = "%y-%m-%d"
today = date.today() 
print(today.strftime('datetime'))

'''grid = [['1', '2'], 
        ['3', '4']]

for x, row in enumerate(grid, start = 0):
    for y, col in enumerate(grid, start = 0):
        if grid[x][y] == '2': 
            print('yes')'''

grid = [ ["-", "-", "-", "#", "#"], 
         ["-", "#", "-", "-", "-"], 
         ["-", "-", "#", "-", "-"], 
         ["-", "#", "#", "-", "-"], 
         ["-", "-", "-", "-", "-"] ]


len_rows = len(grid)

for row in range(len_rows): 
    len_col = len(grid[row])

'''for x, row in enumerate(grid, start = 0):
    for y, col in enumerate(grid, start = 0):
        if grid[x][y] == '-':
            if x != 0 and y != 0 and grid[x-1][y-1] == '#': 
                grid[x][y] = 'Y'
                #count += 1'''


for x, row in enumerate(grid, start = 0):
    for y, col in enumerate(grid, start = 0):
        if grid[x][y] == '-':
            count = 0
            if x != 0 and y != 0 and grid[x-1][y-1] == '#': 
                count += 1
                
            if x != 0 and grid[x-1][y] == '#': 
                count += 1

            if x != 0 and y != len_col - 1 and grid[x-1][y+1] == '#':
                count += 1 

            grid[x][y] = count

print(grid)
                
                
        
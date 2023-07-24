# This programme takes a grid of '#' and '-', and 
# returns a grid where each dash is replaced by a digit 
# indicating the number of #'s immediately adjacent to  the dash
 
grid = [ ["-", "-", "-", "#", "#"], 
         ["-", "#", "-", "-", "-"], 
         ["-", "-", "#", "-", "-"], 
         ["-", "#", "#", "-", "-"], 
         ["-", "-", "-", "-", "-"] ]

len_rows = len(grid)  # number of rows

for row in range(len_rows): 
    len_col = len(grid[row]) # number of columns

# This piece of code iterates over each item on the list, 
# checks if the item is a dash,
# counts the number of hashtags colse to the dash 
# and replaces each dash with the appropriate number

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
        
            if y != 0 and grid[x][y-1] == '#':
                count += 1

            if y != len_col-1 and grid[x][y+1] == '#':
                count += 1

            if x != len_rows - 1 and y != 0 and grid[x+1][y-1] == '#':
                count += 1

            if x != len_rows - 1 and grid[x+1][y] == '#':
                count += 1

            if x != len_rows - 1 and y != len_col - 1 and grid[x+1][y+1] == '#':
                count += 1 

            grid[x][y] = count

print(grid)


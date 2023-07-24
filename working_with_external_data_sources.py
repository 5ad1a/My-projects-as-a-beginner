f = open('input.txt', 'r')

lines = f.readlines()
print(lines)

for l in lines: 
    s = l.strip()
    j = l.split()
    print(s)
    print(j)
n = 1
num = []
for n in range(1,201): 
    num.append(n)
    n += 1

x = input('num: ')
i = 0
for i in range(200):
    if num[i] == x: 
        print('y')

list = [str(i) for i in range(11)]
print(list)
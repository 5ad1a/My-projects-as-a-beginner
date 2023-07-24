#This programme creates two Text Files that contain integers from the smallest to the largest (up to 100)
#It then combines the numbers from both these files sorted from the smallest to the largest in a third Text file

i = 0
with open('numbers1.txt', 'w') as a:
    for i in range(101):
        a.write(str(i)+'\n')
        i +=1
a.close()
    
    
x = 0
with open('numbers2.txt', 'w') as b:
    for x in range(101):
        b.write(str(x)+'\n')
        x +=1
b.close()


file_1 = open('numbers1.txt', 'r')
list_1 = file_1.readlines()

new_list_1 = []

y = 0
for y in range(len(list_1)): 
    new_list_1.append(int(list_1[y].strip()))
    y+=1 


file_2 = open('numbers2.txt', 'r')
list_2 = file_2.readlines()

new_list_2 = []

z = 0
for z in range(len(list_2)): 
    new_list_2.append(int(list_2[z].strip()))
    z+=1 


new_list_1.extend(new_list_2)
new_list_1.sort()

print(new_list_1)

s = 0
with open('all_numbers.txt', 'w') as m: 
    for s in range(len(new_list_1)): 
        m.write(str(new_list_1[s])+'\n')
        s += 1
m.close()

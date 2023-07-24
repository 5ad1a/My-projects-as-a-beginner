#This programme prints all the integers from 1 to 1000
num1000 = list(range(1, 1001))
print(num1000)


print()
print()

#This programme prints all the even numbers from 1 to 1000
even_num = []
for i in num1000: 
    if i%2==0:
        even_num.append(i)

print(even_num)

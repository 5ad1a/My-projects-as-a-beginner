#The code asks the user to enter a number 
#It then calculate the sum of all the even numbers up to or including that number

num = float(input('Please enter a number: '))

count = 0 
sum = 0 

while count <= num: 
    sum += count
    count += 2 
print(sum)

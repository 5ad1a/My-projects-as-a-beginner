num1 = 1
num2 = 2
num3 = 3 

if num1>num2: 
    print(num1)
else: 
    print(num2)

if num1%2==0: 
    print(num1 +' is even.')
else:
    print(num1 +' is odd.')


if num1 > num2 and num2 > num3:
    print(num1, num2, num3)
elif num1 > num2 and num3 > num2:
    print(num1, num3, num2)
elif num3>num1 and num2> num1:
    print(num3, num2, num1)
elif num2>num1 and num3>num1: 
    print(num2, num3, num1)
elif num3>num2 and num1>num2: 
    print(num3, num1, num2)
else: 
    print(num2, num1, num3)
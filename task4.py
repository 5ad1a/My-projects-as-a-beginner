num = int(input('Enter an integer: '))

if num%2==0 and num%5==0: 
    print('Divisible by 2 and 5.')

if num%2==0 or num%5==0:
    print('Divisible by 2 or 5.')

if not num%2==0 or not num%5==0:
    print('Not divisible by 2 or 5.')
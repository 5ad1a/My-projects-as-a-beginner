print('Enter the values for two positive integers a and b to find their Greatest Common Divisor (GCD).')
print()
a = int(input('a: '))
b = int(input('b: '))

if a > b: 
    while b != 0:
        c = b 
        b = a % b 
        a = c
        if b == 0 and a != 0: 
            print(f"The GCD is {a}.")

if a < b: 
    while a != 0:
        c = a
        a = b % a 
        b = c
        if a == 0 and b != 0: 
            print(f"The GCD is {b}.") 

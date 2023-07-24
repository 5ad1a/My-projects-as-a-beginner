number_builder = ""
i = 0

while i <= 50:
    if i % 2 == 0:
        number_builder += str(i) + " "
    i += 1
print(number_builder)

num = []
x = 0
while x <= 50:
    if x % 2 == 0:
        num.append(str(x))
    x += 1
print(' '.join(num))

string = 'This is a sentence'
x = 6
print(string[x].upper())
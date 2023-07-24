str_manip = input('Please enter a sentence: ')

str_len = len(str_manip)

print(str_len)

last_letter = str_manip[str_len-1]

print(str_manip.replace(last_letter, '@'))
print(str_manip[str_len:str_len-4:-1])
print(str_manip[:3]+str_manip[str_len-2:str_len])

print(str_manip.replace(' ', '\n'))

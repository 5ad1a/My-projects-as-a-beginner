string = 'This is a simple sentence'

#This code turns each alternative charachter an uppercase charachter in a sentence 
# and each other alternative character a lowercase chracater
#PSEUDOCODE
#Turn the even indexes into uppercase charachters 
#Turn the odd indexes into lowercase characters

new_string = ""
x = 0 
while x < len(string): 
    if x%2==0: 
        new_string += string[x].upper()
    if x%2!=0: 
        new_string += string[x].lower()
    x += 1
print(new_string)


#This code turns into uppercase characters each alternative word in a sentence 
# and turn into lower case letters each other alternative words
#PSEUDOCODE
#turn the sentence into a list of words
#Turn the even indexes into words with uppercase charachters 
#Turn the odd indexes into words with lowercase characters

list_of_words = string.split()
new_sent = ""
y = 0 
while y < len(list_of_words): 
    if y%2==0: 
        new_sent += list_of_words[y].lower() + ' '
    if y%2!=0: 
        new_sent += list_of_words[y].upper() + ' '
    y += 1
print(new_sent)

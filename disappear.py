#This programme removes the characters selected by an user from a sentence input by the user

sentence = input('Please enter a sentence: ')
print()
print('Enter the character that you want to remove from the sentence, enter \"none\" if you want no more characters to be removed. ')
while True:
    char = (input('Enter: ')).lower()
    if char == 'none': 
        break
    sentence = sentence.replace(char, '')
    
print(sentence)
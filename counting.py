#This programme counts the number of times each character of the alphabet occurs in a string

string = (str(input('Enter a word or a sentence: '))).lower()

alphabet = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j':0, 'k': 0, 'l': 0, 
'm': 0, 'n': 0, 'o':0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}

keys = alphabet.keys()

for i in string: 
    if i in keys: 
        alphabet[i] += 1 

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

for letter in letters: 
    if alphabet[letter] == 0: 
        del alphabet[letter]
        
print(alphabet)
#This programme asks the user to input a sentence
#It outputs each word of the sentence on a new line

sentence = input('Please enter a sentence: ')
list = sentence.split()
print('\n'.join(list))
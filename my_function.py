#This function prints all the days of the week

def week():
    days = 'Monday\nTuesday\nWednesday\nThursday\nFriday\nSaturday\nSunday\n'
    return days

print(week())

#The user is asked to input a sentence
sentence = str(input('Enter a sentence: '))

#This function outputs the sentence with every second word replaced by the word "Hello"
def replace(sentence):
    words_list = sentence.split()
    for x in range(len(words_list)): 
        if x%2!= 0:
            words_list[x] = 'Hello'
    new_sent = " ".join(words_list)
    return new_sent
print(replace(sentence))
    

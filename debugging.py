#k is not defined, so we need to use a variable that is defined.
#If we iterate over the keys we will output only the value of the first key in the dictionary.
#If we put the keys in a list then we can choose which keys' values to output using the index of the key in the key list

def print_values_of(dictionary, keys):    
    for key in keys:
        value = dictionary[key]
        print(value) 
        
#need to escape the apostrophe in "d'oh" using a backlash
simpson_catch_phrases = {"lisa": "BAAAAAART!", "bart": "Eat My Shorts!", "marge": "Mmm~mmmmm", "homer": 'd\'oh!', "maggie": " (Pacifier Suck)"}

#We need to make a list of the keys of the dictionary simpson_catch_phrases
#characters_list = list(simpson_catch_phrases.keys()) 

#The funtion print_values_of() will only print the values of the first, second, and fourth keys in order in the dictionary
a = print_values_of(simpson_catch_phrases, ['lisa', 'bart', 'homer']) 

print(a)

'''
Expected console output:

BAAAAAART!
Eat My Shorts!
d'oh!

'''

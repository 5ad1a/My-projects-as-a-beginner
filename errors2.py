animal = 'lion'   #Syntax error: the value of the variable should be in brackets, logical error: the word lion should be all in lowercase
animal_type = "cub"
number_of_teeth = 16

full_spec = f"This is a {animal}. It is a {animal_type} and it has {number_of_teeth} teeth."  #Logical error: variables in wrong order and missing full stop at the end of the sentence, runtime error: need to add f before the first bracket

print(full_spec) #Syntax error: missing brackets
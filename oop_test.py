class Students: 
    def __init__(self, age, name, gender): 
        self.age = age 
        self.name = name 
        self.gender = gender 
class Sent:
    list = []
    def sentence(name, age, gender):
        s = f'{name} is {age} and is a {gender}.\n'
        list.append(s)


Sarah = Students(19, 'Sarah Montgomery', 'Female')
John = Students(19, 'John Smith', 'Male')

#print(Sarah.sentence())

name = input('Name: ')
age = input('Age: ')
gender = input('Gender: ')
new_student = Students(age, name, gender)
new_student.sentence()

print(list)
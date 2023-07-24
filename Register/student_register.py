#This programme asks the user to enter the number of students who will register for an exam venue
#It then asks the user to input the ID number of each students only once
#The programme writes the ID number of eahc student on a Text FIle followed by a dotted line for signing in as an attendance register

num = [ str(n) for n in range(1,201)]

num_students = input('Please enter the number of students who are registering for the exam: ')

while True:
    if num_students not in num: 
        num_students = input('Please enter a valid number from 1 to 200: ')
    if num_students in num:
        print('\n' +'Enter the ID number of each student once only.'+'\n')
        break
      
i=0 
with open('reg_form.txt', 'w') as f: 
    for i in range(int(num_students)): 
        ID_num = str(input('Enter ID number: '))
        f.write(str(ID_num) +': .................................'+'\n')   
        i += 1 
        if i == int(num_students): 
            break
        
f.close()

print('\n\nFinished!')


import StudentClass as sc

# studentID = input('\n\nYour student ID? ')
# name = input('What is your name? ').title()
# dob = input('Input your DOB (YYY-MM-DD)? ')
# classification = input('What is your classification? ').title()

# student1 = sc.Student(studentID, name, dob, classification)

student1 = sc.Student(892785235, 'Emm Odu', '2018-07-15', 'F')


print()

print('-' * 50)
print(student1.get_name_n_studID()[0], "--", student1.get_name_n_studID()[1])     
print('-' * 50)

print(f'{"Student Age:":18}', student1.get_age())
print(f'{"Registration Date:":18}', student1.get_regDate())

print()
# 1 
# У компанії є кілька відділів. Список працівників для кожного відділу має такий вигляд:
# ['Robert Stivenson,28', 'Alex Denver,30']
# Це список рядків із прізвищем та віком співробітника, розділеними комами.
# Реалізуйте функцію запису даних про співробітників у файл, щоб інформація про кожного співробітника починалася з нового рядка.

def write_employees_to_file(employee_list, path): 
  employers_string = ""
  for dep in employee_list:
    for empl in dep:
      employers_string = employers_string + empl + "\n"
    # print(dep)
  # print("emploers", employers_string)

  f = open(path, "w")
  try:
    f.write(employers_string)
    # print("written")
  finally:
    f.close()
    # print("closed")

# write_employees_to_file([['Robert Stivenson,28', 'Alex Denver,30'], ['Drake Mikelsson,19']], "data.txt")
# write_employees_to_file([['Alex Korp,28', 'Boris Britva,33'], ['Max Pain,29']], "data2.txt")
#-------------------------------------------------------------------------------


# 2
# У попередній задачі ми записали співробітників у файл у такому вигляді:
#   Robert Stivenson,28
#   Alex Denver,30
#   Drake Mikelsson,19
# Виконаємо тепер зворотнє завдання і створимо функцію read_employees_from_file(path), яка читатиме дані з файлу та повертатиме список співробітників у вигляді:
# ['Robert Stivenson,28', 'Alex Denver,30', 'Drake Mikelsson,19']
def read_employees_from_file(path):
    f = open(path, "r")
    try:
        employees_string = f.read()
#        print(employees_string)
    finally:
        f.close()
    employees = employees_string.split("\n")

# check for ""
    for e in employees:
        if e == "":
            employees.remove('')
#    print(employees)
    return employees

#read_employees_from_file("data.txt")
#-------------------------------------------------------------------------------



#3
# Реалізуйте функцію add_employee_to_file(record, path), 
# яка у файл (path) буде додавати співробітника (record) у вигляді рядка "Drake Mikelsson,19".
def add_employee_to_file(record, path):
    f = open(path, "a")
    try:
        f.write(record + "\n")   

    finally:
        f.close()

# add_employee_to_file("Boss Boss, 19", "data.txt")
#-------------------------------------------------------------------------------


#4
# Ми маємо таку структуру файлу:  60b90c1c13067a15887e1ae1,Tayson,3   /...
# Розробіть функцію get_cats_info(path), яка повертатиме список словників із даними котів у вигляді:
# [ {"id": "60b90c1c13067a15887e1ae1", "name": "Tayson", "age": "3"}, ... ]
def get_cats_info(path):
  with open(path, 'r') as file:
    lines = file.readlines()
  
  list = []
  for line in lines:
    splited_line = line.split(',')
    splited_n = splited_line[2].split('\n')
    dict = {"id": splited_line[0], "name": splited_line[1], "age": splited_n[0]}
    list.append(dict)

  return list
#-------------------------------------------------------------------------------


#5
# Розробіть функцію sanitize_file(source, output), що переписує у текстовий файл output
# вміст текстового файлу source, очищений від цифр.
import re 
def sanitize_file(source, output):
    with open(source, 'r') as source:
        text = source.read()
        print(text)
        clean_text = re.sub(r'\d', '', text)
        print(clean_text)
    
    with open(output, 'w') as output:
        output.write(clean_text)

sanitize_file('data.txt', 'data2.txt')
#-------------------------------------------------------------------------------


#5
# Розробіть функцію save_applicant_data(source, output), яка буде вказаний список 
# із параметра source зберігати у файл із параметра output
def save_applicant_data(source, output):
    text = ''
    for student in source:
        for key, value in student.items():
            if key == "eng":
                text += str(value) + "\n"
            else:
                text += str(value) + ","
    print(text)

    with open(output, 'w') as output:
        output.write(text)

# source = [
#     {
#         "name": "Kovalchuk Oleksiy",
#         "specialty": 301,
#         "math": 175,
#         "lang": 180,
#         "eng": 155,
#     },
#     {
#         "name": "Ivanchuk Boryslav",
#         "specialty": 101,
#         "math": 135,
#         "lang": 150,
#         "eng": 165,
#     },
#     {
#         "name": "Karpenko Dmitro",
#         "specialty": 201,
#         "math": 155,
#         "lang": 175,
#         "eng": 185,
#     },
# ]
        
# save_applicant_data(source, 'data.txt')
#-------------------------------------------------------------------------------


#6
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
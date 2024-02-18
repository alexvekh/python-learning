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


#6
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


#7
''' 
Є два рядки у різних кодуваннях - "utf-8" та "utf-16". 
Нам необхідно зрозуміти, чи дорівнюються рядки між собою.

Реалізуйте функцію is_equal_string(utf8_string, utf16_string), 
яка повертає True, якщо рядки дорівнюють собі, і False — якщо ні.
'''
def is_equal_string(utf8_string, utf16_string):
    if utf8_string == utf16_string.decode('utf-16').encode():
        return True
    else:
        return False
#-------------------------------------------------------------------------------


#8
''' 
Дані про користувачів краще зберігати у форматі бінарних файлів. 
Тому вам необхідно створити функцію, яка буде записувати логін та пароль користувача у файл.

Реалізуйте функцію save_credentials_users(path, users_info), 
яка зберігає інформацію про користувачів з паролями в бінарний файл.
Де:
    path – шлях до файлу.
    users_info - словник типу {'andry':'uyro18890D', 'steve':'oppjM13LL9e'}, 
        де ключ — логін (username) користувача, а значення — його пароль (password).
Вимоги:
Кожен рядок файлу повинен мати такий вигляд username:password. 
Такий формат запису використовують при Базовій аутентифікації.
Відкрийте файл для запису та збережіть ключ та значення зі словника users_info 
у вигляді окремого рядка username:password для кожного елемента словника users_info
'''

def save_credentials_users(path, users_info):
    with open(path, 'wb') as file:
        for username, password in users_info.items():
            line = username + ":" + password + '\n'
            #print(line)
            #print(line.encode())
            file.write(line.encode('utf-8'))

#users = {'andry':'uyro18890D', 'steve':'oppjM13LL9e'}
#save_credentials_users("data", users)
#-------------------------------------------------------------------------------


#9
''' 
Реалізуйте функцію get_credentials_users(path), яка повертає список рядків із бінарного файлу, 
створеного в попередньому завданню, де: path – шлях до файлу.
Формат файлу:
    andry:uyro18890D
    steve:oppjM13LL9e
Відкрийте файл для читання, використовуючи with та режим rb. Сформуйте список рядків із файлу та 
поверніть його з функції get_credentials_users у наступному форматі:
['andry:uyro18890D', 'steve:oppjM13LL9e']
Вимоги: Використовуйте менеджер контексту для читання з файлу
'''
def get_credentials_users(path):
    with open(path, 'rb') as file:
        text = file.read()
        list = text.decode("utf-8").split("\n")
    return list

# get_credentials_users("data")
#-------------------------------------------------------------------------------


#10
''' 
Функція повинна працювати так:
Створювати бінарний файл file_name за шляхом path
Зберігати дані словника employee_residence у файл, де кожен новий рядок — це 
ключ значення через пробіл як "Michael Canada"
Архівувати теку по шляху path за допомогою shutil
Ім'я архіву має бути backup_folder.zip
Функція має повернути рядок шляху до архіву backup_folder.zip
Вимоги:
 -запишіть вміст словника employee_residence у бінарний файл з ім'ям file_name 
у теку path за допомогою оператора with.
 - використовуйте символ /, щоб розділити шлях для path та file_name
 - вигляд рядка файлу — Michael Canada, в кінці кожного рядка додається перенесення рядка '\n'.
 - при збереженні кожен рядок файлу кодується методом encode
 =- при записі рядків використовуємо лише метод write
 - архів має бути у форматі zip з ім'ям 'backup_folder', створений за допомогою make_archive.
'''
import shutil
def create_backup(path, file_name, employee_residence):
    print(path, file_name, employee_residence)
    file_path = path + '/' + file_name
    print(file_path)
    with open(file_path, 'wb') as file:
        for employee, residence in employee_residence.items():
            line = employee + ' ' + residence  + '\n'
            print(line)
            file.write(line.encode('utf-8'))
    archive_name = shutil.make_archive('backup_folder', 'zip', path)
    return archive_name

# employee_residence = {'Michael':'Canada', 'Steve':'USA'}
# create_backup("a", "data.bin", employee_residence)
#-------------------------------------------------------------------------------


#11
''' 
Створіть функціонал для розпакування архіву.
Зробіть import пакету shutil
Створіть функцію unpack(archive_path, path_to_unpack), яка викликатиме метод пакета shutil 
unpack_archive та розпаковуватиме архів archive_path у місце path_to_unpack.
Функція нічого не повертає.
'''
import shutil

def unpack(archive_path, path_to_unpack):
    shutil.unpack_archive(archive_path, path_to_unpack)

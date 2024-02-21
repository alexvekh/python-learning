''' 
Для ініціалізації свого проекту створіть допоміжну функцію do_setup(args_dict), 
яка буде викликати функцію setup з параметрами зі словника args_dict.
Структура словника для параметра args_dicts має бути наступною
{
    "name": "useful",
    "version": "1",
    "description": "Very useful code",
    "url": "http://github.com/dummy_user/useful",
    "author": "Flying Circus",
    "author_email": "flyingcircus@example.com",
    "license": "MIT",
    "packages": ["useful"],
}
'''
from setuptools import setup
def do_setup(args_dict):
    setup(**args_dict)
#-------------------------------------------------------------------------------


#2
''' 
Модифікуємо приклад попередньої задачі. 
Для функції do_setup необхідно передбачити другий параметр, який буде списком залежностей.
Функція do_setup(args_dict, requires) повинна викликати функцію setup з параметрами 
зі словника args_dict та параметром install_requires, який набуває значення requires.
'''
from setuptools import setup

def do_setup(args_dict, requires):
    setup(name=args_dict['name'],
          version=args_dict['version'],
          description=args_dict['description'],
          url=args_dict['url'],
          author=args_dict['author'],
          author_email=args_dict['author_email'],
          license=args_dict['license'],
          packages=args_dict['packages'],
          install_requires=requires)

#-------------------------------------------------------------------------------


#3
''' 
Продовжуємо модифікувати приклад. 
Для функції do_setup необхідно передбачити третій параметр, який буде словником, 
де ми можемо вказати список "точок входу" для ключа console_scripts.
'''
from setuptools import setup

def do_setup(args_dict, requires, entry_points):
    setup(name=args_dict['name'],
          version=args_dict['version'],
          description=args_dict['description'],
          url=args_dict['url'],
          author=args_dict['author'],
          author_email=args_dict['author_email'],
          license=args_dict['license'],
          packages=args_dict['packages'],
          install_requires=requires,
          entry_points=entry_points)

#-------------------------------------------------------------------------------


#4
# Напишіть функцію data_preparation, яка приймає набір даних, список списків 
# (Приклад: [[1,2,3],[3,4], [5,6]]).
# Функція повинна видаляти з переданих списків найбільше і найменше значення, але якщо розмір списку 
# понад два елементи. Після видалення даних з кожного списку необхідно злити їх разом в один список, 
# відсортувати його за зменшенням та повернути отриманий список як результат 
# (Для прикладу вище результат буде наступним: [6, 5, 4, 3, 2]).
def data_preparation(list_data):
    data = []
    for list in list_data:
        if len(list) > 2:
            list.remove(max(list))
            list.remove(min(list))
        data.extend(list)
    #print(data)
    data.sort()
    data.reverse()
    #print(data)
    return data
#-------------------------------------------------------------------------------


#5
''' 
Підсписком (sublist) називають список, що є складовою більшого списку. 
Підсписок може містити один елемент, множину елементів або бути порожнім.
Наприклад, [1], [2], [3] та [4] є підсписками списку [1, 2, 3, 4]. 
Список [2, 3] також входить до складу [1, 2, 3, 4], але при цьому список [2, 4] 
не є підсписком [1, 2, 3, 4], оскільки у вихідному списку числа 2 і 4 не є сусідами.
Порожній список є підсписком будь-якого списку.
Напишіть функцію all_sub_lists, що повертає список, який містить всі можливі підсписки заданого.
Наприклад, якщо функції передано аргумент список [1, 2, 3], то функція має повернути 
наступний список: [[], [1], [2], [3], [1, 2], [2, 3], [1, 2, 3]].
Функція all_sub_lists повинна повертати щонайменше один список з порожнім підсписком [[]].
'''
def all_sub_lists(data):
    if data == []:
        return [[]]
    else:
        sub = []
        sub.append([])
        for el in data:
            sub.append([el])
        
        for i in range(len(data)-1):
            sub.append([data[i], data[i + 1]])
        
        for i in range(len(data)-2):
            sub.append([data[i], data[i + 1], data[i + 2]])
        sub.append(data)

    #print(sub)
    return sub

# data = [1, 2, 3]
# all_sub_lists(data)
#-------------------------------------------------------------------------------


#6
# Реалізуйте допоміжну функцію, яка формуватиме запит на сервер у вигляді словника. 
# Дана функція make_request(keys, values) приймає два параметри у вигляді списків. 
# Функція повинна створити словник із ключами з списку keys та значеннями зі списку values.
# Порядок відповідності збігається з індексами списків keys та values.
# Якщо довжина keys та values не збігаються, поверніть порожній словник.
def make_request(keys, values):
    if len(keys) != len(values):
        return {}
    else:
        dict = {}
        for i in range(len(keys)):
            dict[keys[i]] = values[i]
    return dict
#-------------------------------------------------------------------------------


#7
# Реалізуйте функцію file_operations(path, additional_info, start_pos, count_chars), 
# яка додає додаткову інформацію в файл на шляху path з параметра additional_info, 
# і після цього повертає рядок з позиції start_pos довжиною count_chars.
# Вимоги:
#  - функція повинна відкривати файл за допомогою with за шляхом path в режимі додавання інформації
#  - записувати в кінець файлу рядок additional_info
#  - після запису функція має відкрити той самий файл для читання
#  - прочитати та повернути рядок з позиції start_pos завдовжки count_chars за допомогою функції seek.
# Важливо: для проходження завдання необхідно використовувати менеджер контексту with, 
# методи seek, write та read.

def file_operations(path, additional_info, start_pos, count_chars):
    with open(path, 'a') as file:
        file.write(additional_info)
    with open(path, 'r') as file:
        file.seek(start_pos)
        result = file.read(count_chars)
    return result
#-------------------------------------------------------------------------------


#8
# Створіть функцію get_employees_by_profession(path, profession). 
# Функція повинна у файлі (параметр path) знайти всіх співробітників зазначеної професії (параметр profession)
# Вимоги:
#  - відкрийте файл за допомогою with для читання
#  - отримайте рядки з файлу за допомогою методу readlines()
#  - за допомогою методу find знайдіть усі рядки у файлі, де є вказана profession, та помістіть записи до списку
#  - об'єднайте всі ці рядки в списку в один рядок за допомогою методу join (пам'ятайте про символ 
# перенесення рядків '\n' та зайві прогалини, які треба прибрати)
#  - приберіть значення змінної 'profession' (замініть на порожній рядок "" методом replace)
#  - поверніть отриманий рядок із файлу

def get_employees_by_profession(path, profession):
    with open(path, 'r') as file:
        lines = file.readlines()
    #print(lines)
    
    pro_list = []
    for line in lines:
        if line.find(profession) >= 0:
            line = line.replace(' courier\n', '')
            pro_list.append(line)
    #print(pro_list)

    names = ' '.join(pro_list)
    return names

# get_employees_by_profession('data.txt', 'courier')
#-------------------------------------------------------------------------------


#9
# Напишіть функцію to_indexed(source_file, output_file), яка зчитуватиме вміст файлу, 
# додаватиме до прочитаних рядків порядковий номер і зберігати їх у такому вигляді у новому файлі.
# Кожний рядок у створеному файлі повинен починатися з його номера, двокрапки та пробілу, 
# після чого має йти текст рядка з вхідного файлу.
# Нумерація рядків іде від 0.

def to_indexed(source_file, output_file):
    with open(source_file, 'r') as source:
        with open(output_file, 'w') as output:
            count = 0
            for line in source:
                output.write(str(count) + ": " + line)
                count += 1
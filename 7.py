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
# 1
# Розробіть функцію get_days_from_today(date), яка повертатиме кількість днів від поточної дати, 
# де параметр date - це рядок формату '2020-10-09' (рік-місяць-день).
# Підказки:
#  - Параметр date розбити на рік, місяць та день можна використовуючи метод рядків split.
#  - datetime приймає аргументи типу int, використовуйте перетворення типів.
#  - ігноруйте години, хвилини та секунди для вашої дати, важливі повні дні.
#  - кількість днів ви можете отримати відніманням з поточної дати, заданої в змінній date (без часу).
# Наприклад: Якщо поточна дата - '5 травня 2021', то виклик get_days_from_today("2021-10-09") поверне нам -157.

from datetime import datetime

def get_days_from_today(date):
    year, month, day = date.split("-")
    d1 = datetime(year=int(year), month=int(month), day=int(day))
    #print(d1)
    current = datetime.now()
    difference = current - d1
    #print(difference.days)
    return difference.days

#get_days_from_today('2020-10-09')
#-------------------------------------------------------------------------------


#2
# Напишіть функцію визначення кількості днів у конкретному місяці. 
# Ваша функція повинна приймати два параметри: 
#  month - номер місяця у вигляді цілого числа в діапазоні від 1 до 12 
# і year - рік, що складається із чотирьох цифр. 
# Перевірте, чи функція коректно обробляє місяць лютий високосного року.

from datetime import datetime, timedelta

def get_days_in_month(month, year):
    date = datetime(year=year, month=month, day=1)
    if month == 12:
        year += 1
        month = 1
    else:
        month += 1
    date2 = datetime(year=year, month=month, day=1)
    difference = date2 - date
    print(difference.days)
    return difference.days

# get_days_in_month(8, 1999)
#-------------------------------------------------------------------------------


#3
# Напишіть функцію get_str_date(date), яка перетворюватиме дату з бази даних 
# у форматі ISO '2021-05-27 17:08:34.149Z' у вигляді наступного рядка 
# 'Thursday 27 May 2021' - день тижня, число, місяць та рік. 
# Перетворене значення функція повертає під час виклику.

from datetime import datetime

def get_str_date(date):
    d = datetime.strptime(date, '%Y-%m-%d %H:%M:%S.%fZ')
    #print(d)
    string_date = d.strftime('%A %d %B %Y') 
    #print(string_date)
    return string_date

#get_str_date('2021-05-27 17:08:34.149Z')
#-------------------------------------------------------------------------------


#4
# Створіть функцію get_random_winners(quantity, participants), 
# яка повертатиме список унікальних ідентифікаторів бази даних зі словника 
# participants в кількості quantity. Це буде список переможців
# Вимоги:
#  - Отримайте перелік ключів словника. (Після виконання методу keys() 
#     використовуйте перетворення типів)
#  - Перемішайте отриманий список за допомогою методу shuffle
#  - Виберіть випадкових переможців, використовуючи метод sample.
#  - Якщо передана кількість переможців більша за кількість користувачів 
#     (quantity > len(participants)) — поверніть порожній список.
# Наприклад: виклик get_random_winners(2, participants) може повернути список 
# з випадковим набором ідентифікаторів як:
# ['60577ce4b536f8259cc225d2', '605b89080c318d66862db390'].

import random

def get_random_winners(quantity, participants):
    if quantity > len(participants):
        return []
    else:
        participant_id = []
        for p in participants.keys():
            participant_id.append(p)
        random.shuffle(participant_id)
        return random.sample(participant_id, k=quantity)
    
# participants = {
#     "603d2cec9993c627f0982404": "test@test.com",
#     "603f79022922882d30dd7bb6": "test11@test.com",
#     "60577ce4b536f8259cc225d2": "test2@test.com",
#     "605884760742316c07eae603": "vitanlhouse@gmail.com",
#     "605b89080c318d66862db390": "elhe2013@gmail.com",
# }

# get_random_winners(2, participants)
#-------------------------------------------------------------------------------


#5
# Створіть функцію decimal_average(number_list, signs_count), 
# яка обчислюватиме середнє арифметичне типу Decimal 
# з кількістю значущих цифр signs_count. 
# Параметр number_list — список чисел
# Не забувайте приводити всі числа у списку до типу `decimal`

from decimal import Decimal, getcontext

def decimal_average(number_list, signs_count):
    getcontext().prec = signs_count
    sum = Decimal(0)
    for num in number_list:
        sum = sum + Decimal(num)
    return sum / len(number_list)

#print(decimal_average([3, 5, 77, 23, 0.57], 6)) #поверне 21.714
#print(decimal_average([31, 55, 177, 2300, 1.57], 9)) #поверне 512.91400
#-------------------------------------------------------------------------------


#6
# У нас є іменований кортеж для зберігання котів у змінній Cat. 
# На першому місці у нас кличка котика nickname, потім його вік age 
# та ім'я власника кота owner.
# Напишіть функцію convert_list(cats), яка працюватиме у двох режимах.
# Якщо функція convert_list приймає у параметрі cats список іменованих кортежів
# [Cat("Mick", 5, "Sara"), Cat("Barsik", 7, "Olga"), Cat("Simon", 3, "Yura")]
# То функція поверне наступний список словників:
# [
#     {"nickname": "Mick", "age": 5, "owner": "Sara"},
#     {"nickname": "Barsik", "age": 7, "owner": "Olga"},
#     {"nickname": "Simon", "age": 3, "owner": "Yura"},
# ]
# І в той же час, якщо функція convert_list приймає в параметрі cats список словників, 
# то результатом буде зворотна операція та функція поверне список іменованих кортежів.
# Для визначення типу параметра cats використовуйте функцію isinstance.

import collections

Cat = collections.namedtuple("Cat", ["nickname", "age", "owner"])

def is_map_list(list):
    return all(isinstance(item, dict) for item in list)

def is_tuple_list(list): 
    return all(isinstance(item, tuple) for item in list)

def convert_list(cats):
    if is_map_list(cats):
        new_list = []
        for cat in cats:
            new_list.append(Cat(nickname=cat["nickname"], age=cat['age'], owner=cat['owner']))

    if is_tuple_list(cats):
        new_list = []
        for cat in cats:
            new_list.append({"nickname": cat.nickname, "age": cat.age, "owner": cat.owner})

    return new_list        

# cats =  [Cat("Mick", 5, "Sara"), Cat("Barsik", 7, "Olga"), Cat("Simon", 3, "Yura")]
# cats2 = [
#     {"nickname": "Mick", "age": 5, "owner": "Sara"},
#     {"nickname": "Barsik", "age": 7, "owner": "Olga"},
#     {"nickname": "Simon", "age": 3, "owner": "Yura"},
# ]

# print(convert_list(cats))
# print(convert_list(cats2))
#-------------------------------------------------------------------------------


#7
# Є список IP адрес: IP = ["85.157.172.253", ...]
# Реалізуйте дві функції. 
# Перша get_count_visits_from_ip за допомогою Counter повертатиме словник, 
# де ключ це IP, а значення – кількість входжень у вказаний список.
# Приклад: {'85.157.172.253': 2, ... }
# Друга функція get_frequent_visit_from_ip повертає кортеж з найбільш часто 
# уживаним в списку IP і кількістю його появ в списку.
# Приклад: ('66.50.38.43', 4)

from collections import Counter


def get_count_visits_from_ip(ips):
    return Counter(ips)

def get_frequent_visit_from_ip(ips):
    most_common = Counter(ips)
    most_common_list = most_common.most_common(1)
    # most_common_list = Counter(ips).most_common(1)
    return most_common_list[0]
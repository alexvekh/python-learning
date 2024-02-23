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


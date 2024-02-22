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
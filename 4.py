# 1
# У нас є список показань заборгованостей з комунальних послуг наприкінці місяця. Заборгованості можуть бути від'ємними — у нас переплата, чи додатними, якщо необхідно сплатити за рахунками. Напишіть функцію amount_payment, яка приймає на вхід список платежів, підсумовує додатні значення та повертає суму платежу наприкінці місяця.

def amount_payment(payment):
    amount = 0
    for p in payment:
        if p > 0:
            amount += p
    return amount

# 2
# При аналізі даних часто виникає необхідність позбавитися екстремальних значень, перш ніж почати працювати з даними далі. Напишіть функцію prepare_data, яка видаляє з переданого списку найбільше та найменше значення, сортує його в порядку зростання і повертає змінений список як результат.

def prepare_data(data):
    sorted_data = sorted(data)
    sorted_data.pop()
    sorted_data.pop(0)
    return sorted_data


# 3 
# Реалізуйте дві функції. Перша буде використовуватись у бухгалтерії при розрахунку стипендії, get_grade приймає ключ у вигляді оцінки ECTS, і має повертати відповідну п'ятибальну оцінку (перший стовпчик таблиці). Друга get_description теж приймає ключ у вигляді оцінки ECTS, але повертатиме пояснення оцінки в текстовому форматі (останній стовпчик таблиці) і буде використана в електронній заліковій книжці студента. На відсутній ключ функції повинні повертати значення None .

def get_grade(key):
    grades = {
        "F": 1, 
        "FX": 2, 
        "E": 3, 
        "D": 3, 
        "C": 4, 
        "B": 5, 
        "A": 5}
    return grades.get(key)

def get_description(key):
    grades = {
        "F": "Unsatisfactorily", 
        "FX": "Unsatisfactorily", 
        "E": "Enough", 
        "D": "Satisfactorily", 
        "C": "Good", 
        "B": "Very good", 
        "A": "Perfectly"}
    return grades.get(key)

# 4
# Як ми знаємо, ключ у словнику має бути унікальним, тоді як значення його ні. Реалізуйте функцію lookup_key для пошуку всіх ключів за значенням у словнику. Першим параметром у функцію ми передаємо словник, а другим — значення, що хочемо знайти. Таким чином, результат може бути як список ключів, так і порожній список, якщо ми нічого не знайдемо.
def lookup_key(data, value):
    list = []
    for key, v in data.items():
        if v == value:
            list.append(key)
    return list


# 5
# У нас є список показників студентів групи – це список з отриманими балами з тестування. Необхідно поділити список на дві частини. Напишіть функцію split_list, яка приймає список (цілі числа), знаходить середнє значення бала у списку та ділить його на два списки. У перший потрапляють значення менше середнього, включаючи середнє значення, тоді як у другий — строго більше від середнього. Функція повертає кортеж цих двох списків. Для порожнього списку повертаємо два порожні списки.

def split_list(grade):
    over_middle_list = []
    under_middle_list = []

    sum = 0
    count = 0
    for g in grade:
        sum = sum + g
        count = count + 1

    if count == 0:
        return ([], [])
    else:
        middle_grade = sum / count

        for g in grade:
            if g <= middle_grade:
                under_middle_list.append(g)
            else:
                over_middle_list.append(g)
    
        tuple = (under_middle_list, over_middle_list)
     
        return tuple
# print(split_list([1, 12, 3, 24, 5]))

# 6
# Потрібно написати функцію реалізації наступного ігрового алгоритму. На вхід функції game подається два аргументи: список, що складається зі списків, та початкове значення power - енергія гравця. Внутрішні списки — це списки з числовим значенням енергії, які може поглинути гравець, якщо вони менші або дорівнюють його енергії. Після поглинання елементу списку він рухається за списком далі та, або поглинає список повністю до кінця, або, якщо знаходить енергію вище за власну, залишає його і переходить до наступного списку. Наприкінці обходу всіх списків функція повинна повернути загальну отриману енергію гравця.
def game(terra, power):
    for list in terra:
        for energy in list:
            if energy <= power:
                power += energy
            else:
                break
    return power

# 7
# Всім відомо, що для доступу до кредитної картки банку потрібний пін-код. Класично склалося, що це поєднання чотири цифри. Нам необхідно вирішити наступне програмістське завдання. Є підготовлений перелік пін-кодів. Напишіть функцію is_valid_pin_codes, яка буде приймати як параметр список цих пін-кодів — рядок з чотирьох цифр і повертати логічне значення — валідний список чи ні. Переконайтеся, що серед цих пін-кодів у списку не буде дублікатів, всі вони зберігаються у вигляді рядків, їх довжина дорівнює 4 символам і містять вони тільки цифри.
# Приклад аргументу для функції is_valid_pin_codes: ['1101', '9034', '0011'] Якщо список відповідає всім поставленим умовам, функція повертає логічне значення True. Якщо хоч одну з умов порушено, повертається значення — False. Передбачити перевірку на порожній список в аргументі функції та повернути при цьому значення False.

def is_valid_pin_codes(pin_codes):
    if len(pin_codes) == 0:
        return False

    pin_set = set()
    for pin in pin_codes:
        if not isinstance(pin, str):
            return False
        if len(pin) != 4:
            return False
        try:
            int(pin)
        except ValueError:
            return False
        if pin in pin_set:
            return False
        else:
            pin_set.add(pin)
    else:
        return True
print(is_valid_pin_codes(['1101', '9034', '0011']))

# 8
# Другий етап. Необхідно написати функцію is_valid_password, яка перевірятиме отриманий параметр — пароль на надійність.
# Критерії надійного пароля:
#  -Довжина рядка пароля вісім символів.
#  -Містить хоча б одну літеру у верхньому регістрі.
#  -Містить хоча б одну літеру у нижньому регістрі.
#  -Містить хоча б одну цифру.
# Функція is_valid_password повинна повернути True, якщо переданий параметр пароль відповідає вимогам на надійність. Інакше повернути False.

def is_valid_password(password):
    if len(password) < 8:
        return False
    else:
        is3true = set()
        for ch in password:
            if ch.isupper():
                is3true.add("U")
            elif ch.islower():
                is3true.add("L")
            else:
                try:
                    int(ch)              
                    is3true.add("N")
                except ValueError:
                    ch
    if len(is3true) == 3:
        return True
    else:
        return False

# 9
# Напишіть функцію parse_folder, вона приймає єдиний параметр path, який є об'єктом Path. Функція повинна просканувати директорію path та повернути кортеж із двох списків. Перший — це список файлів усередині директорії, другий — список директорій.
    
#from pathlib import Path
def parse_folder(path):
    files = []
    folders = []

    for i in path.iterdir():
        if i.is_dir():
            folders.append(i.name)
        else:
            files.append(i.name)

    return files, folders

# 10
# Створіть функцію parse_args, яка повертає рядок, складений з аргументів командного рядка, розділених пробілами. Наприклад, якщо скрипт був викликаний командою: python run.py first second, то функція parse_args повинна повернути рядок наступного виду 'first second'.

import sys

def parse_args():
    result = ""
    sys.argv.pop(0)     # delete [0]
    is_1_arg = True
    for arg in sys.argv:
        if is_1_arg:
            is_1_arg = False
            result = result + arg
        else:
            result = result + " " + arg    
    
    return result
print(parse_args())

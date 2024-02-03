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
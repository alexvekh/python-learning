# 1
# Напишіть функцію real_len, яка підраховує та повертає довжину рядка без наступних керівних символів: [\n, \f, \r, \t, \v]
def real_len(text):
    control_chars = set("\n\f\r\t\v")
    len = 0
    for ch in text:
        if ch not in control_chars:
            len += 1
    return len

# print(real_len('Alex\nKdfe23\t\f\v.\r'))
#-------------------------------------------------------------------------------


# 2
# Необхідно реалізувати функцію sanitize_phone_number, яка прийматиме рядок з телефонним номером та буде нормалізувати його, тобто. буде прибирати символи (, -, ), + та пробіли.
def sanitize_phone_number(phone):
    return phone.strip().replace("-", "").replace("(", "").replace(")", "").replace("+", "").replace(" ", "")
        
# print(sanitize_phone_number("    +38(050)123-32-34"))
# print(sanitize_phone_number("     0503451234"))
# print(sanitize_phone_number("(050)8889900"))
# print(sanitize_phone_number("38050-111-22-22"))
# print(sanitize_phone_number("38050 111 22 11   "))
#-------------------------------------------------------------------------------


# 3
# напишемо функцію is_check_name, яка приймає два параметри (fullname, first_name) і повертає логічне значення True або False. Це результат перевірки, чи є рядок first_name префіксом рядка fullname. Функція is_check_name чутлива до регістру літер, тобто "Sam" і "sam" для неї різні імена.
def is_check_name(fullname, first_name):
      # Перевірка довжини
#    if len(first_name) > len(fullname):
#        return False
  
    for i in range(len(first_name)):
        if fullname[i] != first_name[i]:
            return False

    return True    

# print(is_check_name('Max Old', 'Alex'))
#-------------------------------------------------------------------------------

# 4
# Приймати список телефонних номерів.
# Санітизувати (нормалізувати) отриманий список телефонів клієнтів за допомогою нашої функції sanitize_phone_number.
# Сортувати телефонні номери за вказаними у таблиці країнами.
# Повертати словник зі списками телефонних номерів для кожної країни у такому вигляді:

def sanitize_phone_number(phone):
    new_phone = (
        phone.strip()
        .removeprefix("+")
        .replace("(", "")
        .replace(")", "")
        .replace("-", "")
        .replace(" ", "")
    )
    return new_phone

def get_phone_numbers_for_countries(list_phones):
    
    jp_phones = []
    tw_phones = []
    sg_phones = []
    ua_phones = []
    phone_map = {"UA": ua_phones,"JP": jp_phones, "TW": tw_phones, "SG": sg_phones}
    
    #sorted_phones = sorted(list_phones)
    for duty_phone in list_phones:
        phone = sanitize_phone_number(duty_phone)

        if phone.startswith("81"):
            jp_phones.append(phone)
        elif phone.startswith("88"):
            tw_phones.append(phone)
        elif phone.startswith("65"):
            sg_phones.append(phone)
        else:
            ua_phones.append(phone)

    return phone_map

# print(get_phone_numbers_for_countries(['380998759405', '657658976', '818765347', '8867658976']))
# print(get_phone_numbers_for_countries(['(65)765-89-77', '(81)8765347', '065-875-94-11', '657658976', '8867658976']))
#-------------------------------------------------------------------------------


# 5
# За допомогою функції zip, за аналогією прикладу теорії, створіть словник TRANS для транслітерації. 
# Створюйте словник TRANS поза функцією translate
# Напишіть функцію translate, яка проводить транслітерацію кириличного алфавіту на латинську.
# Функція translate: приймає на вхід рядок та повертає рядок; проводить транслітерацію кириличних символів на латиницю;
CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
TRANSLATION = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
               "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "ya", "je", "i", "ji", "g")
TRANS = dict()
for cyrilic_symbol, latin_symbol in zip(CYRILLIC_SYMBOLS, TRANSLATION):
    TRANS[ord(cyrilic_symbol)] = latin_symbol
    TRANS[ord(cyrilic_symbol.upper())] = latin_symbol.upper()
#print(TRANS)
def translate(name):
    return name.translate(TRANS)
#print(translate("Дмитро Короб"))  # Dmitro Korob
#print(translate("Олекса Івасюк"))  # Oleksa Ivasyuk


#  Словник TRANS створенний не вірно!
TRANS = {}
def translate(name):
    for c, l in zip(CYRILLIC_SYMBOLS, TRANSLATION):
        TRANS[ord(c)] = l
        TRANS[ord(c.upper())] = l.upper()
    return name.translate(TRANS)

##  Словник TRANS створенний не вірно!
TRANS = dict(zip(CYRILLIC_SYMBOLS, TRANSLATION))
def translate(name):
    translated = ""
    for char in name:
        translated += TRANS.get(char, char)
    return translated
#-------------------------------------------------------------------------------


# 6
#  Напишіть функцію formatted_grades, яка приймає на вхід словник оцінювання студентів за предмет наступного вигляду:
# students = {"Nick": "A", "Olga": "B", "Mike": "FX", "Anna": "C"}
# І повертає список відформатованих рядків, щоб під час виведення наступного коду:
#    1|Nick      |  A  |  5
#    2|Olga      |  B  |  5
#    3|Mike      | FX  |  2
#    4|Anna      |  C  |  4
grades = {"A": 5, "B": 5, "C": 4, "D": 3, "E": 3, "FX": 2, "F": 1}

def formatted_grades(students):
    formatted_students = []
    count = 1 
    for key, value in students.items():
        #print('{:>4}|{:<10}|{:^5}|{:^5}'.format(count, key, value, grades[value]))
        #print(f'{count:>4}|{key:<10}|{value:^5}|{grades[value]:^5}')
        formatted_students.append('{:>4}|{:<10}|{:^5}|{:^5}'.format(count, key, value, grades[value]))
        count += 1
    return formatted_students

# students = {"Nick": "A", "Olga": "B", "Mike": "FX", "Anna": "C"}
# for el in formatted_grades(students):
#     print(el)
#-------------------------------------------------------------------------------


# 7
# Напишіть функцію formatted_numbers, яка повертає список відформатованих рядків, щоб під час виведення наступного коду:
#   for el in formatted_numbers():
#       print(el)
# Виходила наступна таблиця:
# | decimal  |   hex    |  binary  |
# |0         |    0     |         0|
# |1         |    1     |         1|
# |2         |    2     |        10|
# ...  ...  ... to 15

def formatted_numbers():
    table = []
    table.append('|{:^10}|{:^10}|{:^10}|'.format("decimal", "hex", "binary"))
    for i in range (16):
        table.append('|{:<10}|{:^10x}|{:>10b}|'.format(i , i, i))
    return table
# for el in formatted_numbers():
#     print(el)
#-------------------------------------------------------------------------------


# 8
# Напишіть функцію find_word, яка приймає два параметри: перший text та другий word. 
# Функція виконує пошук зазначеного слова word у тексті text за допомогою функції search 
# та повертає словник.
# {
#     'result': True,
#     'first_index': 34,
#     'last_index': 40,
#     'search_string': 'Python',
#     'string': 'Guido van Rossum began working on Python in the late 1980s, as a successor to the ABC programming language, and first released it in 1991 as Python 0.9.0.'
# }
# де:
#   result — результат пошуку True або False
#   first_index — початкова позиція збігу
#   last_index — кінцева позиція збігу
#   search_string — частина рядка, в якому був збіг
#   string — рядок, переданий у функцію

import re

def find_word(text, word):
    d = dict()
    if re.search(word, text):
        d['result'] = True
        matches = re.search(word, text)
        d["first_index"], d["last_index"] = matches.span()
    else:
        d['result'] = False
        d["first_index"] = None
        d["last_index"] = None

    d["search_string"] = word
    d["string"] = text
    return d

# print(find_word(
#     "Guido van Rossum began working on Python in the late 1980s, as a successor to the ABC programming language, and first released it in 1991 as Python 0.9.0.",
#     "Python"))
#-------------------------------------------------------------------------------


# 9
# напишіть функцію find_all_words, яка шукає збіг слова в тексті. 
# Функція повертає список всіх знаходжень слова в параметрі word в тексті у вигляді будь-якого написання, 
# тобто, наприклад, можливі варіанти написання слова "Python" як pYthoN, pythOn, PYTHOn і т.і. 
# головне, щоб зберігався порядок слів, регістр не має значення.
# 
# Підказка: функції модуля re приймають ще ключовий параметр flags 
# і ми можемо визначити нечутливість до регістру, надавши йому значення re.IGNORECASE

import re

def find_all_words(text, word):
    return re.findall(word, text, flags=re.IGNORECASE)
#-------------------------------------------------------------------------------


# 10
# застосуємо функцію sub модуля re для заміни вказаних у списку стоп-слів на деякий шаблон. 
# Наприклад, всі "погані" слова замінюватимемо зірочками. 
# Напишіть функцію replace_spam_words, яка приймає рядок (параметр text), перевіряє його на вміст 
# заборонених слів зі списку (параметр spam_words), та повертає результат рядок, але замість заборонених слів, 
# підставлений шаблон з *, причому довжина шаблону дорівнює довжині забороненого слова. 
# Визначити нечутливість до регістру стоп-слів.
import re

def replace_spam_words(text, spam_words):
    for word in spam_words:
        print(text)
        text = re.sub(word, "*" * len(word), text, flags=re.IGNORECASE)
        print(text)
    return text
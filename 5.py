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

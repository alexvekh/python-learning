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
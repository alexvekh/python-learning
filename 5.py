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

# 2
# Необхідно реалізувати функцію sanitize_phone_number, яка прийматиме рядок з телефонним номером та буде нормалізувати його, тобто. буде прибирати символи (, -, ), + та пробіли.
def sanitize_phone_number(phone):
    return phone.strip().replace("-", "").replace("(", "").replace(")", "").replace("+", "").replace(" ", "")
        
# print(sanitize_phone_number("    +38(050)123-32-34"))
# print(sanitize_phone_number("     0503451234"))
# print(sanitize_phone_number("(050)8889900"))
# print(sanitize_phone_number("38050-111-22-22"))
# print(sanitize_phone_number("38050 111 22 11   "))


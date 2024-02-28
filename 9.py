# Завдання 1
# Реалізуйте функцію вищого порядку get_student_grade, яка приймає параметр option. 
# Якщо він дорівнює значенням "grade", то функція повертає функцію get_grade, 
# а якщо його значення дорівнює "description", то повертає функцію get_description. 
# Якщо параметр за значенням не співпав із заданим - None.

def get_grade(key):
    grade = {"A": 5, "B": 5, "C": 4, "D": 3, "E": 3, "FX": 2, "F": 1}
    return grade.get(key, None)


def get_description(key):
    description = {
        "A": "Perfectly",
        "B": "Very good",
        "C": "Good",
        "D": "Satisfactorily",
        "E": "Enough",
        "FX": "Unsatisfactorily",
        "F": "Unsatisfactorily",
    }
    return description.get(key, None)


def get_student_grade(option):
    if option == "grade":
        return get_grade
    elif option == "description":
        return get_description
    else:
        return None
#-------------------------------------------------------------------------------


# Завдання 2
# Реалізуйте функцію get_discount_price_customer для розрахунку ціни на товар інтернет-магазину 
# з урахуванням знижки клієнта.
# Ви маєте глобальну змінну DEFAULT_DISCOUNT, яка визначає знижку для клієнта, 
# якщо у нього немає поля discount.
# Функція get_discount_price_customer має повертати нову ціну товару для клієнта.
    
DEFAULT_DISCOUNT = 0.05

# def get_discount_price_customer(price, customer):
#   if customer.get("discount") is not None:
#     DEFAULT_DISCOUNT = customer.get("discount")
#   new_price = price * (1 - DEFAULT_DISCOUNT)
#   return new_price
# Why it no work?

def get_discount_price_customer(price, customer):
    try:
        discount = customer['discount']
    except KeyError:
        discount = DEFAULT_DISCOUNT  

    return price * (1 - discount)

# print(get_discount_price_customer(10, {'name': 'Boris', 'discount': 0.15}))
# print(get_discount_price_customer(10, {'name': 'Boris'}))
#-------------------------------------------------------------------------------


# Завдання 3
# GPT helped
# Створіть функцію caching_fibonacci(), яка матиме кеш із попередньо обчисленими значеннями 
# чисел Фібоначі. Усередині вона містить функцію fibonacci(n), яка безпосередньо 
# і обчислюватиме саме число Фібоначчі. 
# Функція caching_fibonacci() повертає функцію fibonacci
# Якщо число Фібоначчі зберігається у словнику cache, то функція fibonacci повертає число 
# з кеша. Якщо його немає у кеші, то ми обчислюємо число і поміщаємо його в кеш, 
# і повертаємо з функції fibonacci.

def caching_fibonacci():
    cache = {}

    def fibonacci(n):
        if n in cache:
            return cache[n]
       
        if n <= 1:
            result = n
        else:
            result = fibonacci(n-1) + fibonacci(n-2) 

        cache[n] = result
        return result

    return fibonacci

# fibonacci = caching_fibonacci()

# print(fibonacci(0)) # 0
# print(fibonacci(1)) # 1
# print(fibonacci(5)) # 5
# print(fibonacci(10)) # 55

# print(cache) # {0: 0, 1: 1, 5: 5, 10: 55}
#-------------------------------------------------------------------------------


# Завдання 4
# GPT helped
# Створіть функцію discount_price(discount), яка визначатиме в собі та повертатиме 
# функцію розрахунку реальної ціни з урахуванням знижки.
# Виклик функції discount_price(discount) поверне функцію, яка розраховує 
# ціну на товар зі знижкою, що дорівнює discount .

def discount_price(discount):
    def calculate(price):
        return price * (1 - discount)
    return calculate

# cost_15 = discount_price(0.15)
# cost_10 = discount_price(0.10)
# cost_05 = discount_price(0.05)

# price = 100
# print(cost_15(price))   # 85.0
# print(cost_10(price))   # 90.0
# print(cost_05(price))   # 95.0
# print(discount_price(0.3)(200))     # 140.0 
#-------------------------------------------------------------------------------


# Завдання 5
# Декоратор повинен додавати для коротких номерів префікс +38, 
# а для повного міжнародного номера (з 12 символом) - тільки знак +. 
# Реалізуйте декоратор format_phone_number для функції sanitize_phone_number 
# з необхідним функціоналом.

def format_phone_number(func):
    def inner(phone):
        new_phone = func(phone)
        if len(new_phone) == 12:
            return "+"+new_phone
        else:
            return "+38"+new_phone 
    return inner
        
@format_phone_number
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
#-------------------------------------------------------------------------------


# Завдання 6
# Є список name з іменами користувачів, але всі починаються з малої літери.
# name = ["dan", "jane", "steve", "mike"]
# Розробіть функцію normal_name, яка приймає список імен та повертає теж список імен, 
# але вже з правильними іменами з великої літери.
# ['Dan', 'Jane', 'Steve', 'Mike']
# Необхідно використовувати функцію map. 
# Не забудьте, що необхідно виконати перетворення типів для map.

def normal_name(list_name):
    names = []
    for i in map(lambda name: names.append(name.title()), list_name):
        pass
    return names
    
# name = ["dan", "jane", "steve", "mike"]
# print(normal_name(name))
#-------------------------------------------------------------------------------


# Завдання 7
# Є список contacts, елементи якого - словники контактів наступного виду:
# {
#     "name": "Allen Raymond",
#     "email": "nulla.ante@vestibul.co.uk",
#     "phone": "(992) 914-3792",
#     "favorite": False,
# }
# Словник містить ім'я користувача, його email, телефонний номер та властивість - 
# обраний контакт чи ні.
# Розробіть функцію get_emails, яка отримує у параметрі список list_contacts 
# та повертає список, який містить електронні адреси всіх контактів зі списку 
# list_contacts. 
# Використовуйте функцію map.

def get_emails(list_contacts):
    emails = []
    for email in map(lambda contact: contact.get("email"), list_contacts):
        emails.append(email)
    return emails

# list = [
#     {
#     "name": "Allen Raynd",
#     "email": "nulla.ante@vestibul.co.uk",
#     "phone": "(992) 914-3792",
#     "favorite": False,
#     },
#     {
#     "name": "Allen Rond",
#     "email": "nulla@vestibul.co.uk",
#     "phone": "(992) 914-3792",
#     "favorite": False,
#     },
#     {
#     "name": "Allen Rymond",
#     "email": "ante@vestibul.co.uk",
#     "phone": "(992) 914-3792",
#     "favorite": False,
#     }
# ]
# print(get_emails(list))
#-------------------------------------------------------------------------------


# Завдання 8
# На початку четвертого модуля ми вирішували завдання виплат за комунальними платежами.
# Вони являли собою список payment з додатними та від'ємними значеннями. 
# Створіть функцію positive_values та за допомогою функції filter відфільтруйте 
# список payment за додатними значеннями, та поверніть його з функції.
# payment = [100, -3, 400, 35, -100]

def positive_values(list_payment):
    positive_payments = []
    for payment in filter(lambda num: num > 0, list_payment):
        positive_payments.append(payment)
    return positive_payments

# payment = [100, -3, 400, 35, -100]
# print(positive_values(payment))
#-------------------------------------------------------------------------------


# Завдання 9
# Створіть функцію get_favorites(contacts), яка повертатиме список, 
# який містить лише обрані контакти. Використовуйте при цьому функцію filter, 
# щоб відфільтрувати по полю favorite лише обрані контакти.

def get_favorites(contacts):
    favorites = []
    for contact in filter(lambda contact: contact.get("favorite"), contacts):
        favorites.append(contact)
    return favorites

# Test
# list = [
#     {
#     "name": "Allen Raynd",
#     "email": "nulla.ante@vestibul.co.uk",
#     "phone": "(992) 914-3792",
#     "favorite": False,
#     },
#     {
#     "name": "Allen Rond",
#     "email": "nulla@vestibul.co.uk",
#     "phone": "(992) 914-3792",
#     "favorite": True,
#     },
#     {
#     "name": "Allen Rymond",
#     "email": "ante@vestibul.co.uk",
#     "phone": "(992) 914-3792",
#     "favorite": True,
#     }
# ]
# print(get_favorites(list))
#-------------------------------------------------------------------------------


# Завдання 10
# Для списку numbers підрахувати суму елементів за допомогою функції reduce.
# numbers = [3, 4, 6, 9, 34, 12]
# Створіть функцію sum_numbers(numbers), результатом виконання якої буде 
# сума чисел всіх елементів списку numbers.
from functools import reduce

def sum_numbers(numbers):
    return reduce(lambda x, y: x + y, numbers)

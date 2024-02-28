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
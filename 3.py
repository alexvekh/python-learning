# 3.5
def get_fullname(first_name, last_name, middle_name=""):
    if middle_name:
        return first_name + " " + middle_name + " " + last_name
    else:
        return first_name + " " + last_name

# 3.6
def first(size, *args):
    return size + len(args)

def second(size, **key_args):
    return size + len(key_args)

# 3.7
def cost_delivery(quantity, *some, discount=0):
  if quantity:
    cost = (3 + (quantity * 2))
  if discount:
    cost = cost * discount
  return cost 

# 3.8
def cost_delivery(quantity, *_, discount=0):
    """Функція повертає суму за доставлення замовлення.

     Перший параметр &mdash; кількість товарів в замовленні.
     Параметр знижки discount, який передається лише як ключовий, за замовчуванням має значення 0."""
    result = (5 + 2 * (quantity - 1)) * (1 - discount)
    return result

# 3.9
def factorial(n):
    if n < 2:
        return 1  # Базовий випадок
    else:
        return n * factorial(n - 1)  # Рекурсивний випадок

def number_of_groups(n, k):
    return round(factorial(n) / (factorial(n - k) * factorial(k)))
    # n! / ((n - k)! · k!)

@# 3.10
def fibonacci(n):
    if n == 0:
        return 0  # Базовий випадок
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)  # Рекурсивний випадок
        # Fn = Fn-1 + Fn-2.
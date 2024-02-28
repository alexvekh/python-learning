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




# def fibonacci(n):
#     if n == 0:
#         return 0  # Базовий випадок
#     elif n == 1:
#         return 1
#     else:
#         return fibonacci(n - 1) + fibonacci(n - 2)  # Рекурсивний випадок
#         # Fn = Fn-1 + Fn-2.
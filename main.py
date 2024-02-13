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

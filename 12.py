# Assigment 1
# Розробіть дві функції для серіалізації та десеріалізації списку контактів 
# за допомогою пакета json та зберігання отриманих даних у бінарному файлі.
# Перша функція write_contacts_to_file приймає два параметри: filename - ім'я файлу, 
# contacts - список контактів. Вона зберігає вказаний список у файл, 
# використовуючи метод dump пакету json .
# Друга функція read_contacts_from_file читає та повертає зазначений список contacts 
# з файлу filename, використовуючи метод load пакету json .

import pickle

def write_contacts_to_file(filename, contacts):
    with open(filename, 'wb') as file:
        pickle.dump(contacts, file)

def read_contacts_from_file(filename):
    with open(filename, 'rb') as file:
        contacts_copy = pickle.load(file)
        return contacts_copy

# Test    
# contacts = [
#     "name": "Allen Raymond",
#     "email": "nulla.ante@vestibul.co.uk",
#     "phone": "(992) 914-3792",
#     "favorite": False,
#   },

    
# filename = 'data2.txt'
# write_contacts_to_file(filename, contacts)
# print(read_contacts_from_file(filename))
#-------------------------------------------------------------------------------


# Assigment 2
# Розробіть дві функції для серіалізації та десеріалізації списку контактів 
# за допомогою пакета pickle та зберігання отриманих даних у текстовому файлі.
# Перша функція write_contacts_to_file приймає два параметри: filename - ім'я файлу, 
# contacts - список контактів. Вона зберігає вказаний список у файл, 
# використовуючи метод dump пакету pickle.
# Друга функція read_contacts_from_file читає та повертає зазначений список contacts 
# з файлу filename, використовуючи метод load пакету pickle.

import json

def write_contacts_to_file(filename, contacts):
    with open(filename, 'w') as file:
        json.dump({"contacts": contacts}, file)   # extra in to "contacts": 

def read_contacts_from_file(filename):
    with open(filename, 'r') as file:
        contacts_copy = json.load(file)
        print(contacts_copy)
        return contacts_copy['contacts']  # to get from "contacts"

#Test    
# contacts = [
#     {'name': 'Allen Raymond', 'email': 'nulla.ante@vestibul.co.uk', 'phone': '(992) 914-3792', 'favorite': False},
#     {'name': 'Chaim Lewis', 'email': 'dui.in@egetlacus.ca', 'phone': '(294) 840-6685', 'favorite': False}
# ]
# filename = 'data2.json'
# write_contacts_to_file(filename, contacts)
# print(read_contacts_from_file(filename))
#-------------------------------------------------------------------------------


# Assigment 3
# Розробіть дві функції для серіалізації та десеріалізації списку контактів 
# за допомогою пакета csv та зберігання отриманих даних у текстовому файлі.

import csv

def write_contacts_to_file(filename, contacts):
    field_names = []
    for key in contacts[0].keys():
        field_names.append(key)
    with open(filename, 'w', newline='') as file:   
        writer = csv.DictWriter(file, fieldnames=field_names)
        writer.writeheader()
        for i in range(len(contacts)):
            writer.writerow(contacts[i])

def str_to_bool(str): # my func
    if str == "False":
        return False
    else:
        return True

def read_contacts_from_file(filename):
    with open(filename, 'r', newline='') as file:
        reader = csv.DictReader(file)
        rows = []
        for row in reader:
            row['favorite'] = str_to_bool(row['favorite']) # used my fumc
            rows.append(row)
        return rows

#  # Test    
# contacts = [
#     {'name': 'Allen Raymond', 'email': 'nulla.ante@vestibul.co.uk', 'phone': '(992) 914-3792', 'favorite': False},
#     {'name': 'Chaim Lewis', 'email': 'dui.in@egetlacus.ca', 'phone': '(294) 840-6685', 'favorite': False}
# ]
# #print(contacts)
# filename = 'data.csv'
# write_contacts_to_file(filename, contacts)
# print(read_contacts_from_file(filename))
#-------------------------------------------------------------------------------


# Assigment 4
# Розробіть клас Person. 
# Розробіть клас Contacts.
# Розробіть два методи для серіалізації та десеріалізації екземпляра 
# класу Contacts за допомогою пакету pickle та зберігання даних у бінарному файлі.

class Person:
    def __init__(self, name: str, email: str, phone: str, favorite: bool):
        self.name = name
        self.email = email
        self.phone = phone
        self.favorite = favorite 

class Contacts:
    def __init__(self, filename: str, contacts: list[Person] = None):
        if contacts is None:
            contacts = []
        else:
            self.contacts = contacts
        self.filename = filename

    def save_to_file(self):
        with open(self.filename, 'wb') as file:
            pickle.dump(self, file)

    def read_from_file(self):
        with open(self.filename, 'rb') as file:
            contacts_loaded = pickle.load(file)
            return contacts_loaded

# contacts = [
#     Person(
#         "Allen Raymond",
#         "nulla.ante@vestibul.co.uk",
#         "(992) 914-3792",
#         False,
#     ),
#     Person(
#         "Chaim Lewis",
#         "dui.in@egetlacus.ca",
#         "(294) 840-6685",
#         False,
#     ),
# ]

# persons = Contacts("user_class.dat", contacts)
# persons.save_to_file()
# person_from_file = persons.read_from_file()
# print(person_from_file)
# print(persons == person_from_file)  # False
# print(persons.contacts[0] == person_from_file.contacts[0])  # False
# print(persons.contacts[0].name == person_from_file.contacts[0].name)  # True
# print(persons.contacts[0].email == person_from_file.contacts[0].email)  # True
# print(persons.contacts[0].phone == person_from_file.contacts[0].phone)  # True

#-------------------------------------------------------------------------------


# Assigment 5
# Додайте до класу Contacts атрибут count_save, за замовчуванням він повинен мати значення 0. 
# Реалізуйте магічний метод __getstate__ для класу Contacts. 
# При упаковуванні екземпляра метод класу повинен збільшувати значення атрибута count_save на одиницю. 
# Таким чином, ця властивість - лічильник повторних операцій пакування екземпляра класу

import pickle


class Person:
    def __init__(self, name: str, email: str, phone: str, favorite: bool):
        self.name = name
        self.email = email
        self.phone = phone
        self.favorite = favorite

class Contacts:
   
    def __init__(self, filename: str, contacts: list[Person] = None):
        if contacts is None:
            contacts = []
        self.filename = filename
        self.contacts = contacts
        self.count_save = 0

    def save_to_file(self):
        with open(self.filename, "wb") as file:
            pickle.dump(self, file)

    def read_from_file(self):
        with open(self.filename, "rb") as file:
            content = pickle.load(file)
        return content

    def __getstate__(self):
        copy = self.__dict__.copy()
        copy['count_save'] += 1
        return copy

contacts = [
    Person(
        "Allen Raymond",
        "nulla.ante@vestibul.co.uk",
        "(992) 914-3792",
        False,
    ),
    Person(
        "Chaim Lewis",
        "dui.in@egetlacus.ca",
        "(294) 840-6685",
        False,
    ),
]

persons = Contacts("user_class.dat", contacts)
persons.save_to_file()
first = persons.read_from_file()
first.save_to_file()
second = first.read_from_file()
second.save_to_file()
third = second.read_from_file()

print(persons.count_save)  # 0
print(first.count_save)  # 1
print(second.count_save)  # 2
print(third.count_save)  # 3
#-------------------------------------------------------------------------------


# Assigment 6
# Додайте до класу Contacts атрибут count_save, за замовчуванням він повинен мати значення 0. 
# Реалізуйте магічний метод __getstate__ для класу Contacts. 
# При упаковуванні екземпляра метод класу повинен збільшувати значення атрибута count_save на одиницю. 
# Таким чином, ця властивість - лічильник повторних операцій пакування екземпляра класу

import pickle


class Person:
    def __init__(self, name: str, email: str, phone: str, favorite: bool):
        self.name = name
        self.email = email
        self.phone = phone
        self.favorite = favorite

class Contacts:
   
    def __init__(self, filename: str, contacts: list[Person] = None):
        if contacts is None:
            contacts = []
        self.filename = filename
        self.contacts = contacts
        self.count_save = 0
        self.is_unpacking = False           # is_unpacking

    def save_to_file(self):
        with open(self.filename, "wb") as file:
            pickle.dump(self, file)

    def read_from_file(self):
        with open(self.filename, "rb") as file:
            content = pickle.load(file)
        return content

    def __getstate__(self):
        copy = self.__dict__.copy()
        copy['count_save'] += 1
        return copy
    
    def __setstate__(self, value):
        self.__dict__ = value
        self.is_unpacking = True            # is_unpacking = True

contacts = [
    Person(
        "Allen Raymond",
        "nulla.ante@vestibul.co.uk",
        "(992) 914-3792",
        False,
    ),
    Person(
        "Chaim Lewis",
        "dui.in@egetlacus.ca",
        "(294) 840-6685",
        False,
    ),
]

persons = Contacts("user_class.dat", contacts)
persons.save_to_file()
person_from_file = persons.read_from_file()
print(persons.is_unpacking)  # False
print(person_from_file.is_unpacking)  # True
#-------------------------------------------------------------------------------


# Assigment 7



#-------------------------------------------------------------------------------


# Assigment 8



#-------------------------------------------------------------------------------


# Assigment 9


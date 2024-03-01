# Assigment 1
# Створіть клас Animal. Також створіть екземпляр класу Animal (замість реалізації 
# класу можете використовувати pass) і привласніть змінній animal.
class Animal:
    color = ""
    legs = 4

animal = Animal()
#-------------------------------------------------------------------------------


# Assigment 2
# Створіть клас Animal. Також створіть екземпляр класу Animal та привласніть 
# змінній animal. Для класу Animal у конструкторі створіть дві властивості: 
# nickname - кличка тварини та weight - вага тварини. 
# Реалізуйте також метод класу say. 

class Animal:
    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight
    def say():
        print(' I am {animal.nickname}, {animal.weight} lb')

animal = Animal("Boris", 12)

# Test
# print(animal)
#-------------------------------------------------------------------------------


# Assigment 3
# Для попереднього завдання реалізуйте в класі Animal метод change_weight, 
# який має змінювати вагу тварини.
# Викличте функцію change_weight(12) для об'єкта animal та змініть значення 
# початкової ваги з 10 на 12 одиниць.

class Animal:
    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight

    def say(self):
        pass

    def change_weight(self, weight):
        self.weight = weight

animal = Animal("Simon", 10)
animal.change_weight(12)

# Test
# print(animal.weight)
#-------------------------------------------------------------------------------


# Assigment 4
# Додамо в клас Animal змінну класу color, значення якої спочатку дорівнює 'white', 
# і метод change_color, який повинен змінювати значення змінної класу color.
# Створіть екземпляри об'єкта: first_animal та second_animal
# Викличте функцію change_color("red") для будь-якого екземпляра об'єкту 
# Animal та змініть значення змінної класу color на "red".

class Animal:
    color = "white"

    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight

    def say(self):
        pass

    def change_color(self, color):
        Animal.color = color
        # self.__class__.color = color      # better

    def change_weight(self, weight):
        self.weight = weight

    
first_animal = Animal("Dog", 7)
second_animal = Animal("Cat", 4)

first_animal.change_color('red')  
print(second_animal.color)
#-------------------------------------------------------------------------------


# Assigment 5
# Створіть клас Cat, батьківським класом якого є клас Animal. 
# У класі Cat виконайте перевизначення методу say, щоб він повертав рядок "Meow" 
# для екземплярів класу Cat.
# Створіть також змінну cat, яка буде екземпляром класу Cat. 
# При створенні змінної cat ім'я кота має бути "Simon", а вага - 10 одиниць.

class Animal:
    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight

    def say(self):
        pass

    def change_weight(self, weight):
        self.weight = weight

class Cat(Animal):
    def say(self):
        return "Meow"
    
cat = Cat('Simon', 10)
print(cat)
#-------------------------------------------------------------------------------


# Assigment 6
# Створіть клас Dog, батьківським класом якого є клас Animal. У класі Dog виконайте 
# перевизначення методу say, щоб він повертав рядок "Woof" для екземплярів класу Dog.
# У конструкторі класу Dog введіть нову властивість breed - порода, 
# при цьому повинні залишитись всі властивості, успадковані від класу Animal.
# Створіть у коді наступний екземпляр класу Dog.

class Animal:
    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight

    def say(self):
        pass

    def change_weight(self, weight):
        self.weight = weight


class Dog(Animal):
    def __init__(self, nickname, weight, breed):
        super().__init__(nickname, weight)
        self.breed = breed
    
    def say(self):
        return 'Woof'

dog = Dog("Barbos", 23, "labrador")
print(dog.bread)
#-------------------------------------------------------------------------------


# Assigment 7
# Для минулого завдання додамо клас Owner — власника собаки. 
# У класу є три атрибути: ім'я — name, вік — age та адреса — address. 
# Також необхідно реалізувати метод info, який повертає словник з ключами 'name', 'age' 
# і 'address', та значення яких дорівнюють відповідним властивостям екземпляра класу.

# Реалізувати для класу Dog атрибут owner, який буде екземпляром класу Owner. 
# Додати до класу Dog метод who_is_owner, який повертає результат виклику методу 
# info екземпляра класу Owner, тобто це словник з ключами name, age та address власника.

class Animal:
    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight

    def say(self):
        pass

    def change_weight(self, weight):
        self.weight = weight

class Owner:    
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address
        
    def info(self):
        return {
            'name': self.name,
            'age': self.age,
            'address': self.address,
            }
        
class Dog(Animal):
    def __init__(self, nickname, weight, breed, owner):
        self.breed = breed
        self.owner = owner     
        super().__init__(nickname, weight)

    def say(self):
        return "Woof"

    def who_is_owner(self):
        return self.owner.info()

#Test       
# alex = Owner('Alex', 40, '20, Fake street')
# dog = Dog('Palkan', 5, 'labrador', alex)
# print(alex.name, dog.nickname)
# print(dog.who_is_owner())
#-------------------------------------------------------------------------------


# Assigment 8
    # Перепишемо завдання розрахунку заборгованостей з комунальних послуг 
# за допомогою класу UserList.
# payment = [1, -3, 4]
# def amount_payment(payment):
#     sum = 0
#     for value in payment:
#         if value > 0:
#             sum = sum + value
#     return sum
# Нагадаємо умову. У нас є список показань заборгованостей з комунальних послуг 
# наприкінці місяця, список payment. Заборгованості можуть бути від'ємними — 
# у нас переплата, або додатними, якщо потрібно сплатити за рахунками.

# Створіть клас AmountPaymentList, успадковуйте його від класу UserList. 
# Зробіть функцію amount_payment методом класу AmountPaymentList.

from collections import UserList


class AmountPaymentList(UserList):
    def amount_payment(self):
        sum = 0
        for value in self:
            if value > 0:
                sum = sum + value
        return sum

#-------------------------------------------------------------------------------


# Assigment 9
# Створіть клас NumberString, успадкуйте його від класу UserString, визначте для нього 
# метод number_count(self), який буде рахувати кількість цифр у рядку.

from collections import UserString

class NumberString(UserString):
    def number_count(self):
        count = 0
        for char in self:
            if char.isdigit():
                count += 1 
        return count
#-------------------------------------------------------------------------------


# Assigment 10
# Створіть клас IDException, який успадковуватиме клас Exception.
# Також реалізуйте функцію add_id(id_list, employee_id), яка додає до списку id_list 
# ідентифікатор користувача employee_id та повертає вказаний оновлений список id_list.
# Функція add_id буде викликати власне виключення IDException, якщо employee_id 
# не починається з '01', інакше employee_id буде додано до списку id_list.

class IDException(Exception):
    pass

def add_id(id_list: [], employee_id: str):
    if employee_id.startswith('01'):
        id_list.append(employee_id)
        return id_list
    else:
        raise IDException

# Test
# print(add_id(['01001'], '02111'))    

#-------------------------------------------------------------------------------


# Assigment 11
# Для коду із завдання вам необхідно реалізувати клас CatDog, не використовуючи 
# успадкування від класу Animal, але щоб екземпляр класу CatDog поводився як і 
# екземпляр класу Cat, тобто. він повинен вдати, що він клас Cat.

class Animal:
    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight

    def say(self):
        pass

    def change_weight(self, weight):
        self.weight = weight


class Cat(Animal):
    def say(self):
        return "Meow"


class CatDog:
    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight

    def say(sef):
        return "MMMMMMMMM-oooooo-fffffff"
    
    def change_weight(self, weight):
        self.weight = weight

#-------------------------------------------------------------------------------


  # Assigment 12
# Реалізуйте клас Contacts, який працюватиме з контактами. На першому етапі ми додамо два методи.
#   list_contacts повертає список контактів це змінна contacts з поточного екземпляра класу
#   add_contacts додає новий контакт до списку, який є змінною об'єкту - contacts
# Contacts.current_id - унік id контакту. 
# Коли ми додаємо новий контакт, то передаємо аргументи в метод # add_contacts: name, phone, email та favorite. 
# Метод повинен створити словник із зазначеними ключами та значеннями параметрів функції. 
# Також необхідно додати до словника новий ключ id, значенням якого є значення змінної класу current_id.
# Приклад отриманого словника:
#     {
#     "id": 1,
#     "name": "Wylie Pope",
#     "phone": "(692) 802-2949",
#     "email": "est@utquamvel.net",
#     "favorite": True,
#     }
# Вказаний словник ми додаємо до списку contacts. 
# Не забуваймо збільшувати змінну current_id на одиницю після кожного виклику методу add_contacts.
# Примітка: для правильного проходження тесту не створюйте екземпляр класу в коді.

class Contacts:
    current_id = 1

    def __init__(self):
        self.contacts = []

    def list_contacts(self):
        return self.contacts

    def add_contacts(self, name, phone, email, favorite):
        contact = {
            "id": self.__class__.current_id, 
            "name": name,
            "phone": phone,
            "email": email,
            "favorite": favorite,
        }
        self.__class__.current_id += 1
        self.contacts.append(contact)

# Test
# contacts = Contacts()
# print(contacts)
# print(contacts.contacts)
# contacts.add_contacts("Wylie Pope", "(692) 802-2949", "est@utquamvel.net", True)
# print(contacts.contacts)
# print(contacts.list_contacts())
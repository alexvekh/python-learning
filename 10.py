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

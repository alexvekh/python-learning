# Assigment 1
# Створіть клас Point, який відповідатиме за відображення геометричної точки на площині.
# Реалізуйте через конструктор __init__ ініціалізацію двох атрибутів: координати x та координати y.
# Приклад:

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
# # Test
# point = Point(5, 10)
# print(point.x)  # 5
# print(point.y)  # 10
        
#-------------------------------------------------------------------------------


# Assigment 2
# У класу Point через конструктор __init__ оголошено два атрибути: координати x та y. 
# Приховати доступ до них з допомогою подвійного підкреслення: __x та __y
# Реалізуйте для класу Point механізми setter та getter до атрибутів __x та __y 
# за допомогою декораторів property та setter.

class Point:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y
    
    @property
    def x(self):
        return self.__x
    
    @x.setter
    def x(self, x):
        self.__x = x

    @property
    def y(self):
        return self.__y
    
    @y.setter
    def y(self, y):
        self.__y = y
        

# # Test
# point = Point(5, 10)
# print(point.x)  # 5
# print(point.y)  # 10
#-------------------------------------------------------------------------------


# Assigment 3
# У класу Point до механізму setter властивостей x і y додайте перевірку на значення, що вводиться. 
# Дозвольте встановлювати значення властивостей x та y для екземпляра класу, тільки якщо вони мають 
# числове значення (int або float).
# Приклад:
# point = Point("a", 10)
# print(point.x)  # None
# print(point.y)  # 10

class Point:
    def __init__(self, x, y):
        self.__x = None
        self.__y = None
        self.x = x
        self.y = y

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if (type(x) == int) or (type(x) == float):
            self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        if (type(y) == int) or (type(y) == float):
            self.__y = y

# # Приклад:
# point = Point("a", 10)
# print(point.x)  # None
# print(point.y)  # 10
#-------------------------------------------------------------------------------


# Assigment 4
class Point:
    def __init__(self, x, y):
        self.__x = None
        self.__y = None
        self.x = x
        self.y = y

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if (type(x) == int) or (type(x) == float):
            self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        if (type(y) == int) or (type(y) == float):
            self.__y = y


class Vector:
    def __init__(self, coordinates: Point):
        self.coordinates = coordinates

    def __setitem__(self, index: int, value: (int, float)):
        if index == 0:
            self.coordinates.x = value
        elif index == 1:
            self.coordinates.y = value
        else:
            raise IndexError("Invalid index for Vector")

    def __getitem__(self, index: int) -> (int, float):
        if index == 0:
            return self.coordinates.x
        elif index == 1:
            return self.coordinates.y
        else:
            raise IndexError("Invalid index for Vector")


vector = Vector(Point(1, 10))

print(vector.coordinates.x)  # 1
print(vector.coordinates.y)  # 10

vector[0] = 10  # Встановлюємо координату x вектора 10

print(vector[0])  # 10
print(vector[1])  # 10
#-------------------------------------------------------------------------------


# Assigment 5
# Реалізуйте для класу Point та Vector магічний метод __str__. 
# Для класу Point метод повинен повертати рядок виду Point(x,y), 
# а для класу Vector - рядок Vector(x,y), як у прикладі нижче 
# (замість x,y необхідно підставити значення координат екземпляра класу):
class Point:
    def __init__(self, x, y):
        self.__x = None
        self.__y = None
        self.x = x
        self.y = y

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if (type(x) == int) or (type(x) == float):
            self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        if (type(y) == int) or (type(y) == float):
            self.__y = y
    
    def __str__(self):
        return f'Point({self.__x}, {self.__y})'


class Vector:
    def __init__(self, coordinates: Point):
        self.coordinates = coordinates


    def __setitem__(self, index, value):
        if index == 0:
            self.coordinates.x = value
        elif index == 1:
            self.coordinates.y = value
        else:
            raise IndexError("Invalid index for Vector")

    def __getitem__(self, index):
        if index == 0:
            return self.coordinates.x
        elif index == 1:
            return self.coordinates.y
        else:
            raise IndexError("Invalid index for Vector")

    def __str__(self):
        return f'Vector({self.coordinates.x}, {self.coordinates.y})'

point = Point(1, 10)
vector = Vector(point)

print(point)  # Point(1,10)
print(vector)  # Vector(1,10)
#-------------------------------------------------------------------------------


# Assigment 6
# Для екземпляра класу Vector реалізуйте функтор. Створіть для класу Vector метод __call__. 
# Він має реалізувати наступну поведінку:
#     vector = Vector(Point(1, 10))
#     print(vector())  # (1, 10)
# При виклику екземпляра класу як функції він повертає кортеж з координатами вектора.
# Якщо при виклику ми передаємо параметр число, ми виконуємо добуток вектора на число — 
# множимо кожну координату на вказане число та повертаємо кортеж з новими координатами вектора.
# vector = Vector(Point(1, 10))
# print(vector(5))  # (5, 50)

class Point:
    def __init__(self, x, y):
        self.__x = None
        self.__y = None
        self.x = x
        self.y = y

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if (type(x) == int) or (type(x) == float):
            self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        if (type(y) == int) or (type(y) == float):
            self.__y = y
    
    def __str__(self):
        return f'Point({self.__x}, {self.__y})'


class Vector:
    def __init__(self, coordinates: Point):
        self.coordinates = coordinates


    def __setitem__(self, index, value):
        if index == 0:
            self.coordinates.x = value
        elif index == 1:
            self.coordinates.y = value
        else:
            raise IndexError("Invalid index for Vector")

    def __getitem__(self, index):
        if index == 0:
            return self.coordinates.x
        elif index == 1:
            return self.coordinates.y
        else:
            raise IndexError("Invalid index for Vector")

    def __call__(self, value=None):
        if value == None:
            value = 1
        return (self.coordinates.x * value, self.coordinates.y * value)



    def __str__(self):
        return f'Vector({self.coordinates.x}, {self.coordinates.y})'

# vector = Vector(Point(1, 10))
# print(vector())  # (1, 10)
# print(vector() == (1, 10))

# vector = Vector(Point(1, 10))
# print(vector(5))  # (5, 50)
    
#-------------------------------------------------------------------------------


# Assigment 7
# Реалізуйте для класу Vector операції додавання та віднімання векторів. 
# Тобто перевизначите для нього математичні оператори __add__ та __sub__
# Є два вектори: a з координатами (x1, y1) та b з координатами (x2, y2).
# Тоді додавання векторів b + a - це новий вектор з координатами (x2 + x1, y2 + y1). 
# Віднімання – зворотна операція, b - a - це новий вектор з координатами (x2 - x1, y2 - y1)

class Point:
    def __init__(self, x, y):
        self.__x = None
        self.__y = None
        self.x = x
        self.y = y

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if (type(x) == int) or (type(x) == float):
            self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        if (type(y) == int) or (type(y) == float):
            self.__y = y
    
    def __str__(self):
        return f'Point({self.__x}, {self.__y})'


class Vector:
    def __init__(self, coordinates: Point):
        self.coordinates = coordinates


    def __setitem__(self, index, value):
        if index == 0:
            self.coordinates.x = value
        elif index == 1:
            self.coordinates.y = value
        else:
            raise IndexError("Invalid index for Vector")

    def __getitem__(self, index):
        if index == 0:
            return self.coordinates.x
        elif index == 1:
            return self.coordinates.y
        else:
            raise IndexError("Invalid index for Vector")

    def __call__(self, value=None):
        if value == None:
            value = 1
        return (self.coordinates.x * value, self.coordinates.y * value)

    def __add__(self, vector):
        new_x = self.coordinates.x + vector.coordinates.x
        new_y = self.coordinates.y + vector.coordinates.y
        return Vector(Point(new_x, new_y))
        
    def __sub__(self, vector):
        new_x = self.coordinates.x - vector.coordinates.x
        new_y = self.coordinates.y - vector.coordinates.y
        return Vector(Point(new_x, new_y))

    def __str__(self):
        return f'Vector({self.coordinates.x}, {self.coordinates.y})'

# vector1 = Vector(Point(1, 10))
# vector2 = Vector(Point(10, 10))

# vector3 = vector2 + vector1
# vector4 = vector2 - vector1

# print(vector3)  # Vector(11,20)
# print(vector4)  # Vector(9,0)

#-------------------------------------------------------------------------------


# Assigment 8
# Реалізуйте для класу Vector операцію скалярного добутку векторів. 
# Тобто перевизначте для нього математичний оператор __mul__
# Є два вектори: a з координатами (x1, y1) та вектор b з координатами (x2, y2).
# Тоді скалярний добуток векторів b*a - це таке число x2*x1+y2*y1.

    def __mul__(self, vector):
        xx = self.coordinates.x * vector.coordinates.x
        yy = self.coordinates.y * vector.coordinates.y
        return xx + yy
# Приклад коду:
# vector1 = Vector(Point(1, 10))
# vector2 = Vector(Point(10, 10))
# scalar = vector2 * vector1
# print(scalar)  # 110
#-------------------------------------------------------------------------------


# Assigment 9
# Перш ніж ми приступимо до операцій порівняння векторів, реалізуйте метод визначення 
# довжини вектора - len для класу Vector
# Для вектора a з координатами (x1, y1) його довжина визначається за такою формулою:
# (x1 ** 2 + y1 ** 2) ** 0.5.
# Приклад коду:
# vector1 = Vector(Point(1, 10))
# vector2 = Vector(Point(10, 10))
# print(vector1.len())  # 10.04987562112089
# print(vector2.len())  # 14.142135623730951

    def len(self):
        return (self.coordinates.x ** 2 + self.coordinates.y ** 2) ** 0.5
    
#-------------------------------------------------------------------------------


# Assigment 10
# Реалізуйте всі методи порівняння для класу Vector. 
# З метою спрощення порівнювати екземпляри класу Vector будемо тільки за їх довжиною, 
# використовуючи метод len, не враховуючи напрямок векторів.
# Приклад коду:
# vector1 = Vector(Point(1, 10))
# vector2 = Vector(Point(3, 10))
# print(vector1 == vector2)  # False
# print(vector1 != vector2)  # True
# print(vector1 > vector2)  # False
# print(vector1 < vector2)  # True
# print(vector1 >= vector2)  # False
# print(vector1 <= vector2)  # True

    def __eq__(self, vector):
        if self.len() == vector.len():
            return True
        else:
            return False
        
    def __ne__(self, vector):
        if self.len() != vector.len():
            return True
        else:
            return False

    def __lt__(self, vector):
        if self.len() < vector.len():
            return True
        else:
            return False

    def __gt__(self, vector):
        if self.len() > vector.len():
            return True
        else:
            return False

    def __le__(self, vector):
        if self.len() <= vector.len():
            return True
        else:
            return False

    def __ge__(self, vector):
        if self.len() >= vector.len():
            return True
        else:
            return False


#-------------------------------------------------------------------------------

# All code
        
class Point:
    def __init__(self, x, y):
        self.__x = None
        self.__y = None
        self.x = x
        self.y = y

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if (type(x) == int) or (type(x) == float):
            self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        if (type(y) == int) or (type(y) == float):
            self.__y = y
    
    def __str__(self):
        return f'Point({self.__x}, {self.__y})'


class Vector:
    def __init__(self, coordinates: Point):
        self.coordinates = coordinates


    def __setitem__(self, index, value):
        if index == 0:
            self.coordinates.x = value
        elif index == 1:
            self.coordinates.y = value
        else:
            raise IndexError("Invalid index for Vector")

    def __getitem__(self, index):
        if index == 0:
            return self.coordinates.x
        elif index == 1:
            return self.coordinates.y
        else:
            raise IndexError("Invalid index for Vector")

    def __call__(self, value=None):
        if value == None:
            value = 1
        return (self.coordinates.x * value, self.coordinates.y * value)

    def __add__(self, vector):
        new_x = self.coordinates.x + vector.coordinates.x
        new_y = self.coordinates.y + vector.coordinates.y
        return Vector(Point(new_x, new_y))
        
    def __sub__(self, vector):
        new_x = self.coordinates.x - vector.coordinates.x
        new_y = self.coordinates.y - vector.coordinates.y
        return Vector(Point(new_x, new_y))

    def __mul__(self, vector):
        xx = self.coordinates.x * vector.coordinates.x
        yy = self.coordinates.y * vector.coordinates.y
        return xx + yy
    
    def len(self):
        return (self.coordinates.x ** 2 + self.coordinates.y ** 2) ** 0.5

    def __str__(self):
        return f'Vector({self.coordinates.x}, {self.coordinates.y})'

    def __eq__(self, vector):
        if self.len() == vector.len():
            return True
        else:
            return False
        
    def __ne__(self, vector):
        if self.len() != vector.len():
            return True
        else:
            return False

    def __lt__(self, vector):
        if self.len() < vector.len():
            return True
        else:
            return False

    def __gt__(self, vector):
        if self.len() > vector.len():
            return True
        else:
            return False

    def __le__(self, vector):
        if self.len() <= vector.len():
            return True
        else:
            return False

    def __ge__(self, vector):
        if self.len() >= vector.len():
            return True
        else:
            return False

vector1 = Vector(Point(1, 10))
vector2 = Vector(Point(3, 10))
print(vector1 == vector2)  # False
print(vector1 != vector2)  # True
print(vector1 > vector2)  # False
print(vector1 < vector2)  # True
print(vector1 >= vector2)  # False
print(vector1 <= vector2)  # True
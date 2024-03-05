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
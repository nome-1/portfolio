class Person:
    def __init__(self, firstName, lastName, idNumber):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber


class Student(Person):
    def __init__(self, firstName, lastName, idNumber):
        super().__init__(firstName, lastName, idNumber)

    def print(self):
        return self.firstName


Stu = Student("bob", "fisher", 40)
print(Stu.print())


class Rectangle:

    def __init__(self, length, width):
        self.length = length
        self.width = width


class Square(Rectangle):

    def __init__(self, length, width):
        super().__init__(length, width)

    def area(self):
        return self.length * self.width


class Cube(Rectangle):

    def __init__(self, length, width, height):
        super().__init__(length, width)
        self.height = height

    def volume(self):
        return self.length * self.width * self.height


square = Square(3, 3)
cube = Cube(3, 3, 3)

print(square.area())
print(cube.volume())

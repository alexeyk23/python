# coding=utf-8
__author__ = 'admin'

# класс точка
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "Coodinates:(" + str(self.x) + ", " + str(self.y) + ")"

# класс прямоугольник
class Rectangle:
    def __init__(self, x, y, a, b):
        self.leftDown = Point(x, y)
        self.leftUp = Point(x, y + b)
        self.rightDown = Point(x + a, y)
        self.rightUp = Point(x + a, y + b)


    def __str__(self):
        return "Coodrinates of square:\n" + self.leftDown.__str__() + '\n' + self.leftUp.__str__() + '\n' + self.rightUp.__str__() + '\n' + self.rightDown.__str__()
    # отображение относительное Ох
    def reflectOx(self):
        self.leftDown.y *= -1
        self.rightUp.y *= -1
        self.leftUp.y *= -1
        self.leftDown.y *= -1
    # отображение относительное Оу
    def reflectOy(self):
        self.leftDown.x *= -1
        self.rightUp.x *= -1
        self.leftUp.x *= -1
        self.leftDown.x *= -1

# класс квадрат
class Square(Rectangle):
    def __init__(self, x, y,a):
         # вызов консткуктора базового класса
        Rectangle.__init__(self, x, y, a, a)

rec = Rectangle(0, 1, 1, 2)

print rec,'\n'
print "reflected about the axis Ox"
rec.reflectOx()
print rec,'\n'

print "reflected about the axis Oy"
rec.reflectOy()
print rec
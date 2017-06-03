class Point:
    def __init__(self,name, x, y):
        self.name = name
        self.x = x
        self.y = y

    def print(self):
        print("Point {0}: x = {1} and y = {2}".format(self.name, self.x, self.y))
        print()

class Rectangle:
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y


    def print(self):
        print("Point {0}: x = {1} and y = {2}".format(self.name, self.x, self.y))
        print()


    def print_area(self, point):
        width = point.x - self.x
        height=  (point.y - self.y)

        self.area = width * height

        print("The area = ", self.area)

    def print_perimeter(self, point):
        width = point.x - self.x
        height=  (point.y - self.y)

        self.perimeter = (width + height) * 2

        print("The perimeter = ", self.perimeter)

    def print_flip(self, point):
        self.width = point.y - self.y
        self.height=  (point.x - self.x)

        print("After flip, The width = {0}, The height = {1}".format(self.width, self.height))


point_1 =  Rectangle("A", 2, 1 )
point_2 = Rectangle ("B", 10, 9)

point = (point_2, point_1,)
point_1.print()
point_2.print()

point_1.print_area(point_2)
point_1.print_perimeter(point_2)

point_1.print_flip(point_2)
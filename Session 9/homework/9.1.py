class Point:
    def __init__(self,name, x, y):
        self.name = name
        self.x = x
        self.y = y

    def print(self):
        print("Point {0}: x = {1} and y = {2}".format(self.name, self.x, self.y))
        print()

    def print_distant(self, point):
        self.distant = ((point.x - self.x) **2 + (point.y - self.y)**2) ** (1/2)


        print("The distant between A and B = ", self.distant)


    def print_halfway(self, point):

        self.halfway_x = (point.x - self.x) / 2
        self.halfway_y = (point.y - self.y) / 2

        print("The midpoint = {0} and {1}".format(self.halfway_x, self.halfway_y))


    # def print_reflect(self):
    #
    #     self.reflect_x = -self.x
    #     self.reflect_y = -self.y
    #
    #     print("The reflect ")




point_1 =  Point("A", 2, 1)
point_2 = Point ("B", 10, 9)

point = (point_2, point_1)


    # def print_point(self):
    #     print("Point = {0}: x = {1} and y = {2}".format(point.name, point.x, point.y))
    #     print()


point_1.print()
point_2.print()

point_1.print_distant(point_2)

point_1.print_halfway(point_2)
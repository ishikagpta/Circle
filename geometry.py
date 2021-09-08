import math


# Circle class is made to represent a circle in the (x, y) coordinate
# plane and to check whether a point is within the circle
class Circle:

    def __init__(self, x=0, y=0, radius=1):
        self.__x = x
        self.__y = y
        if radius <= 0:
            self.__radius = 1
        else:
            self.__radius = radius

    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

    def getRadius(self):
        return self.__radius

    def setX(self, x):
        self.__x = x

    def setY(self, y):
        self.__y = y

    def setRadius(self, radius):
        if radius <= 0:
            self.__radius = 1
        else:
            self.__radius = radius

    def getArea(self):
        return self.__radius ** 2 * math.pi

    def getPerimeter(self):
        return 2 * self.__radius * math.pi

    # isPointWithinCircle returns boolean representing if the specified point (x, y) is within the circle
    def isPointWithinCircle(self, x, y):
        if (x - self.__x) ** 2 + (y - self.__y) ** 2 <= self.__radius ** 2:
            return True
        else:
            return False

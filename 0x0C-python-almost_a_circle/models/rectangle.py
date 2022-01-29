#!/usr/bin/python3
"""
This module has a class Rectangle that inherits Base
"""

Base = __import__("models.base").base.Base
validate_int = __import__("models.base").base.validate_int
validate_not_neg = __import__("models.base").base.validate_not_neg


class Rectangle(Base):
    """
    This class inherits Base, it is for rectangles
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialize the rectangle
        """
        super().__init__(id)
        validate_int("width", width)
        validate_int("height", height)
        self.__width = width
        self.__height = height
        validate_not_neg("x", x)
        validate_not_neg("y", y)
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """
        Returns the width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, width):
        """
        Sets the width of the rectangle
        """
        validate_int("width", width)
        self.__width = width

    @property
    def height(self):
        """
        Returns the height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, height):
        """
        Sets the height of the rectangle
        """
        validate_int("height", height)
        self.__height = height

    @property
    def x(self):
        """
        Gets the value of x
        """
        return self.__x

    @x.setter
    def x(self, num):
        """
        This sets the value of x
        """
        validate_not_neg("x", num)
        self.__x = num

    @property
    def y(self):
        """
        Gets the value of y
        """
        return self.__y

    @y.setter
    def y(self, num):
        """
        Sets the value of y
        """
        validate_not_neg("y", num)
        self.__y = num

    def area(self):
        """
        Returns the area of the rectangle
        """
        return self.__height * self.__width

    def display(self):
        """
        Prints out the rectangle with the offset
        """
        for emptyrow in range(self.__y):
            print('')
        for rows in range(self.__height):
            print("{}{}".format(
                ' ' * self.__x, '#' * self.__width))

    def __str__(self):
        """
        Makes a pretty string of our rectangle object
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """
        Update the rectangle with new arbitrary properties
        """
        newargs = [self.id, self.__width, self.__height, self.__x, self.__y]
        if len(args) > 0:
            for i in range(len(args)):
                newargs[i] = args[i]
        else:
            for i in kwargs:
                if i == "id":
                    newargs[0] = kwargs[i]
                if i == "width":
                    newargs[1] = kwargs[i]
                if i == "height":
                    newargs[2] = kwargs[i]
                if i == "x":
                    newargs[3] = kwargs[i]
                if i == "y":
                    newargs[4] = kwargs[i]
        self.__init__(
            newargs[1], newargs[2], newargs[3], newargs[4], newargs[0])

    def to_dictionary(self):
        """
        Returns a dictionary representation of the object
        """
        return {
            'id': self.id, 'width': self.width, 'height': self.height,
            'x': self.x, 'y': self.y
        }

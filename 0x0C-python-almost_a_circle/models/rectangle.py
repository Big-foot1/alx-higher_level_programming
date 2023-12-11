#!/usr/bin/python3
"""
the class Rectangle that inherits from Base
"""
from .base import Base


class Rectangle(Base):
    """
    A representation of a rectangle
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Init Class
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """
            Width Getter
        """
        return self.__width

    @property
    def height(self):
        """
            height Getter
        """
        return self.__height

    @property
    def x(self):
        """
            x Getter
        """
        return self.__x

    @property
    def y(self):
        """
            y Getter
        """
        return self.__y

    @width.setter
    def width(self, value):
        """
            Width Setter
        Attribute:
            Value(int): value to assign
        Raises:
            TypeError: Value must be int
            ValueError: Value must be > 0
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """
            height Setter
        Attribute:
            Value(int): value to assign
        Raises:
            TypeError: Value must be int
            ValueError: Value must be > 0
        """
        if type(value) is not int:
                raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        """
            x Setter
        Attribute:
            Value(int): value to assign
        Raises:
            TypeError: Value must be int
            ValueError: Value must be >= 0
        """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        """
            Width Setter
        Attribute:
            Value(int): value to assign
        Raises:
            TypeError: Value must be int
            ValueError: Value must be >= 0
        """
        if type(value) is not int:
                raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
            Define The Area of Rectangle
        """
        return self.__width * self.__height

    def display(self):
        """
            Display The Rectangle Using  '#'
        """
        print(("\n" * self.__y) +
              "\n".join(((" " * self.__x) + ("#" * self.__width))
                        for i in range(self.__height)))
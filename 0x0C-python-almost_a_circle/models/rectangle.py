#!/usr/bin/python3
"""Rectangle class"""
from models.base import Base


class Rectangle(Base):
    """class Rectangle"""
    __nb_objects = 0

    def __init__(self, width, height, x=0, y=0, id=None):
        """CONSTRUCTOR"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """class method"""
        return self.__width

    @width.setter
    def width(self, value):
        """class method"""
        self.validate_positive_integer(value, "width")
        self.__width = value

    @property
    def height(self):
        """class method"""
        return self.__height

    @height.setter
    def height(self, value):
        """class method"""
        self.validate_positive_integer(value, "height")
        self.__height = value

    @property
    def x(self):
        """class method"""
        return self.__x

    @x.setter
    def x(self, value):
        """class method"""
        self.validate_non_negative_integer(value, "x")
        self.__x = value

    @property
    def y(self):
        """class method"""
        return self.__y

    @y.setter
    def y(self, value):
        """class method"""
        self.validate_non_negative_integer(value, "y")
        self.__y = value

    def validate_positive_integer(self, value, attribute_name):
        """class method"""
        if not isinstance(value, int):
            raise TypeError(f"{attribute_name} must be an integer")
        if value <= 0:
            raise ValueError(f"{attribute_name} must be > 0")

    def validate_non_negative_integer(self, value, attribute_name):
        """class method"""
        if not isinstance(value, int):
            raise TypeError(f"{attribute_name} must be an integer")
        if value < 0:
            raise ValueError(f"{attribute_name} must be >= 0")

    def area(self):
        """class method"""
        return self.width * self.height

    def display(self):
        """class method"""
        for i in range(self.y):
            print()
        for i in range(self.height):
            print(" " * self.x + '#' * self.width)

    def __str__(self):
        """class method"""
        return "[Rectangle] ({}) {}/{} - {}/{}"\
               .format(self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """class method"""
        attributes = ['id', 'width', 'height', 'x', 'y']
        if args:
            for i in range(len(args)):
                setattr(self, attributes[i], args[i])
        elif kwargs:
            for key, value in kwargs.items():
                if key in attributes:
                    setattr(self, key, value)

    def to_dictionary(self):
        """class method"""
        return {"x": self.x, "y": self.y, "id": self.id, "height": self.height, "width": self.width}

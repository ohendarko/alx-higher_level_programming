#!/usr/bin/python3
"""Square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """class Square"""
    def __init__(self, size, x=0, y=0, id=None):
        """CONSTRUCTOR"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """class method"""
        return self.width

    @size.setter
    def size(self, value):
        """class method"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """class method"""
        if args:
            attrs = ["id", "size", "x", "y"]
            for i, value in enumerate(args):
                setattr(self, attrs[i], value)
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def __str__(self):
        """class method"""
        return "[Square] ({}) {}/{} - {}"\
               .format(self.id, self.x, self.y, self.width)

    def to_dictionary(self):
        """class method"""
        return {"id": self.id, "size": self.size, "x": self.x, "y": self.y}

    def to_csv_row(self):
        """class method"""
        return [self.id, self.width, self.x, self.y]

    @classmethod
    def create_from_csv_row(cls, row):
        """class method"""
        return cls(*map(int, row[1:]), id=int(row[0]))

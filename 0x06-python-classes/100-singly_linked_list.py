#!/usr/bin/python3
""" Each module, class, and
method must contain docstring as comments."""


class Node:
    """ Each module, class, and
    method must contain docstring as comments."""
    def __init__(self, data, next_node=0):
        """ Each module, class, and
        method must contain docstring as comments."""
        if type(data) is not int:
            raise TypeError("data must be an integer")
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """ Each module, class, and
        method must contain docstring as comments."""
        return self.__data

    @property
    def next_node(self):
        """ Each module, class, and
        method must contain docstring as comments."""
        return self.__next_node

    @data.setter
    def data(self, value):
        """ Each module, class, and
        method must contain docstring as comments."""
        if type(value) is not int:
            raise TypeError("data must be an integer")
        self.__data = value

    @next_node.setter
    def next_node(self, value):
        """ Each module, class, and
        method must contain docstring as comments."""
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """ Each module, class, and
    method must contain docstring as comments."""
    def __init__(self):
        """ Each module, class, and
        method must contain docstring as comments."""
        self.__head = None

    def sorted_insert(self, value):
        """ Each module, class, and
        method must contain docstring as comments."""
        new_node = Node(value)
        if self.__head is None or value < self.__head.data:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            current = self.__head
            while current.next_node and current.next_node.data < value:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self):
        """ Each module, class, and
        method must contain docstring as comments."""
        result = ""
        current = self.__head
        while current:
            result += str(current.data)
            current = current.next_node
            if current is not None:
                result += "\n"
        return result

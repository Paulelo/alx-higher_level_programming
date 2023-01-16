#!/usr/bin/python3
""" Creates a node and initializes
set a data in a singly linked list.
All attributes are set to priv
ate using properties """


class Node:
    """ Creates a node and initializes
        set a data in a singly linked list.
        All attributes are set to priv
        ate using properties
    Attributes:
        data (:obj:`int`, optional): data to be stored in current node
        next_node (node) : pointer to next node in list

    """
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Setter checks if TypeError or occured
        before setting value for data"""
        return (self.__data)

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        """Setter checks if TypeError or occured
        before setting value for next_node"""
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value


class SinglyLinkedList:
    """SinglyLinkedList creates a list
    and print it out in sorted order"""
    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        """Sorted_insert inserts a value in current node"""
        new_node = Node(value)
        if self.__head is None:
            self.__head = new_node
            return
        current_node = self.__head
        while True:
            if current_node.next_node is None:
                current_node.next_node = new_node
                break
            current_node = current_node.next_node

    def __repr__(self):
        result = []
        current_node = self.__head
        while current_node is not None:
            result.append(str(current_node.data))
            current_node = current_node.next_node
        result.sort()
        return ("\n".join(result))

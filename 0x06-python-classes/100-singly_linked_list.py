#!/usr/bin/python3
class Node:
    """ Creates a node and initializes
        set a data in a singly linked list.
        All attributes are set to priv
        ate using properties """
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node  = next_node
    @property
    def data(self):
        return (self.__data)
    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        else:
            self.__data = value
    @property
    def next_node(self):
        return (self.__next_node)
    @next_node.setter
    def next_node(self, value):
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value

class SinglyLinkedList:
    def __init__(self):
        self.__head = None
    def sorted_insert(self, value):
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

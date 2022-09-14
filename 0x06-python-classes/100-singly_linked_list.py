class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node
    @property
    def data(self):
        return self.__data
    @data.setter
    def data(self, data):
        if type(data) != int:
            raise TypeError("next_node must be a Node object")
        self.__data = data
    @property
    def next_node(self):
        return self.__next_node
    @next_node.setter
    def next_node(self, next_node):
        if next_node is not None and type(next_node) != Node:
            raise TypeError("next_node must be a Node object")
        self.__next_node = next_node
class SinglyLinkedList:
    def __init__(self):
        self.__head = None
    def sorted_insert(self, value):
        if self.__head is None:
            self.__head = Node(value)
        else:
            current =self.__head
            previous = None
            while current and current.data <= value:
                previous = current
                current = current.next_node
            if not current:
                previous.next_node = Node(value)
            elif not previous and current is self.__head:
                self.__head = Node(value, current)
            elif current.data > value:
                previous.next_node = Node(value, current)
    def __str__(self):
        node = self.__head
        txt = ''
        while True:
            txt += str(node.data)
            node = node.next_node
            if node.next_node is None:
                break
            else:
                txt += '\n'
        return txt

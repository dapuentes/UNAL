class Node:
    def __init__ (self, value, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_value(self, value):
        self.value = value

    def set_next(self, next_node):
        self.next_node = next_node

class LinkedList:
    def __init__(self, value):
        node = Node(value)
        self.head = node
        self.tail = node
        self.length = 1

    def append(self, value):
        node = Node(value)
        if self.length == 0:
            self.head = node
            self.tail = node
        else:            
            self.tail.set_next(node)
            self.tail = node
        self.length += 1
        return True
    
    def invertir(self):
        aux = self.head
        node = None
        while aux:
            node_sig = aux.get_next()
            aux.set_next(node)
            node = aux
            aux = node_sig
        self.head = node

    def print_list(self):
        aux = self.head
        while aux:
            print(aux.get_value())
            aux = aux.get_next()


a = int(input())
b = int(input())
lista = LinkedList(b)
for i in range(a-1):
    c = int(input())
    lista.append(c)
lista.invertir()
lista.print_list()

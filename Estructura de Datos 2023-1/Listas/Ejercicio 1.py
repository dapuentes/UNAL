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

    def print_list(self):
        aux = self.head
        while aux:            
            print(aux.get_value())
            aux = aux.get_next()

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

    def get(self, index):
        if index >= self.length or index < 0:
            return None
        aux = self.head
        for _ in range(index):
            aux = aux.get_next()
        return aux

    def insert(self, index,value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        node = Node(value)
        aux = self.get(index - 1)
        node.set_next(aux.get_next())
        aux.set_next(node)
        self.length += 1
        return True

a = int(input())
b = int(input())
lista = LinkedList(b)
for i in range(a-1):
    c = int(input())
    lista.append(c)
d = int(input())
print(lista.get(d).get_value())
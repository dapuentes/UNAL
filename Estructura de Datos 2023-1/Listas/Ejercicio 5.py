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
    
    def n_ultimate(self, value):
        aux = self.head
        enesimo = None
        cont = 1
        while aux:
            if cont == value:
                enesimo = self.head
            elif cont > value:
                enesimo = enesimo.get_next()
            aux = aux.get_next()
            cont += 1
        if enesimo:
            return enesimo.get_value()
        else:
            None

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
d = int(input())
print(lista.n_ultimate(d))

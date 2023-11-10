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

    def lista_guion(self):
        aux = self.head
        lista_guion = ""
        while aux:            
            lista_guion += str((aux.get_value()))
            aux = aux.get_next()
        print("-".join(lista_guion))

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

    def agregar_par(self, value):
        if value % 2 == 0:
            self.append(value)
    
a = int(input())
b = int(input())
lista = LinkedList(b)
for i in range(a-1):
    c = int(input())
    lista.agregar_par(c)
lista.lista_guion()
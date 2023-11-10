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
            print(aux.get_value(), end='')
            if aux.get_next():
                print("/",end='')
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
    
    def find(self, value):
        aux = self.head
        cont = 0 
        index = None
        while aux:
            if aux.get_value() == value:
                if index is None:
                    print(0)
                else:
                    print(cont - 1)
                return 
            index = aux.get_value()
            aux = aux.get_next()
            cont += 1

    def intercambio(self):
        node3 = self.get(2)
        node7 = self.get(6)
        node4 = self.get(3)
        node8 = self.get(7)

        aux = node3.get_value()
        node3.set_value(node7.get_value())
        node7.set_value(aux)

        aux = node4.get_value()
        node4.set_value(node8.get_value())
        node8.set_value(aux)

         
a = int(input())
lista = LinkedList(a)
for i in range(7):
    c = int(input())
    lista.append(c)
lista.intercambio()
lista.print_list()

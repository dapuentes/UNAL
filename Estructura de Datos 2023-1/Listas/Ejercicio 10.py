#Lista Doble
class Node:
    def __init__(self, value, next_node=None, prev_node=None):
        self.value = value
        self.next_node = next_node
        self.prev_node = prev_node

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value

    def get_next(self):
        return self.next_node

    def set_next(self, next_node):
        self.next_node = next_node

    def get_prev(self):
        return self.prev_node

    def set_prev(self, prev_node):
        self.prev_node = prev_node
    

class DoubleLinkedList:
    
    def __init__(self, value):
        node = Node(value)
        self.head = node
        self.tail = node
        self.length = 1
        
    def get_length (self):
        return self.length
    
    #imprimir    
    def print_list(self):
        aux = self.head
        while aux:
            print(aux.get_value(),end=" ")
            aux = aux.get_next()
        print()

    #agregar al final
    def append(self, value):
        node = Node(value)
        if self.length == 0:
            self.head = node
            self.tail = node
        else:
            self.tail.set_next(node)
            node.set_prev(self.tail) 
            self.tail = node
        self.length += 1
        return True
    
    def ent(self):
        aux = self.head
        s = ""
        while aux:
            s += str(aux.get_value())
            aux = aux.get_next()
        return int(s)
    
    def listas(self, lista):
        sum1 = self.ent()
        sum2 = lista.ent()
        return sum1 + sum2
    
a = int(input())
b = int(input())
lista1 = DoubleLinkedList(b)
for i in range(a-1):
    c = int(input())
    lista1.append(c)
d = int(input())
e = int(input())
lista2 = DoubleLinkedList(e)
for i in range(d-1):
    f = int(input())
    lista2.append(f)

print(lista1.listas(lista2))

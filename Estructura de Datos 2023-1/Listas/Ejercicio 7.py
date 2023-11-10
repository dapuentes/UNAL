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

    #obtener nodo
    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        if index < self.length / 2:
            aux = self.head
            for _ in range(index):
                aux = aux.get_next()
        else:
            aux = self.tail
            for _ in range(self.length - 1, index, -1):
                aux = aux.get_prev()
        return aux

    def palindromo(self):
        aux1 = self.head
        aux2 = self.tail
        while aux1:
            if aux1.get_value() != aux2.get_value():
                return False
            aux1 = aux1.get_next()
            aux2 = aux2.get_prev()
        return True


a = int(input())
b = int(input())
lista = DoubleLinkedList(b)
for i in range(a-1):
    c = int(input())
    lista.append(c)
print(lista.palindromo())
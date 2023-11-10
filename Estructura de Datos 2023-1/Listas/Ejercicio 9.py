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

    def swap(self, value1, value2):
            aux1 = self.head
            aux2 = self.head

            if value1 == value2:
                print("no hace nada")
                return False

            while aux1:
                if aux1.get_value()== value1:
                    break
                aux1 = aux1.get_next()

            while aux2:
                if aux2.get_value()== value2:
                    break
                aux2 = aux2.get_next()

            if not aux1 or not aux2:
                print("no existe uno de los valores")
                return False

            if self.head == aux1:
                self.head = aux2
            elif self.head == aux2:
                self.head = aux1
            if self.tail == aux1:
                self.tail = aux2
            elif self.tail == aux2:
                self.tail = aux1
            
            temp = aux1.get_next()
            aux1.set_next(aux2.get_next())
            aux2.set_next(temp)
            
            if aux1.get_next() != None:
                aux1.get_next().set_prev(aux1)
            if aux2.get_next() != None:
                aux2.get_next().set_prev(aux2)
        
            temp = aux1.get_prev()
            aux1.set_prev(aux2.get_prev())
            aux2.set_prev(temp)

            if aux1.get_prev() != None:
                aux1.get_prev().set_next(aux1)
            if aux2.get_prev() != None:
                aux2.get_prev().set_next(aux2) 

            return True

    def swap_posicion(self, index):
        aux1 = self.head
        aux2 = self.tail

        for i in range(index-1):
             aux1 = aux1.get_next()             
             aux2 = aux2.get_prev()        

        if self.head == aux1:
            self.head = aux2
        elif self.head == aux2:
            self.head = aux1
        if self.tail == aux1:
            self.tail = aux2
        elif self.tail == aux2:
            self.tail = aux1
        
        temp = aux1.get_next()
        aux1.set_next(aux2.get_next())
        aux2.set_next(temp)
        
        if aux1.get_next() != None:
            aux1.get_next().set_prev(aux1)
        if aux2.get_next() != None:
            aux2.get_next().set_prev(aux2)
    
        temp = aux1.get_prev()
        aux1.set_prev(aux2.get_prev())
        aux2.set_prev(temp)

        if aux1.get_prev() != None:
            aux1.get_prev().set_next(aux1)
        if aux2.get_prev() != None:
            aux2.get_prev().set_next(aux2) 

        return True
            
a = int(input())
b = int(input())
lista = DoubleLinkedList(b)
for i in range(a-1):
    c = int(input())
    lista.append(c)
d = int(input())
lista.swap_posicion(d)
lista.print_list()
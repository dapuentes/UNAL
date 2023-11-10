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
    
    def print_list(self):
        aux = self.head
        while aux:
            print(aux.get_value())
            aux = aux.get_next()

    def medium(self):
        fast = self.head
        slow = self.head
        while fast:
            fast = fast.get_next()
            if fast:
                fast = fast.get_next()
                slow = slow.get_next()
        return slow

    def inter_med(self):
      aux = self.head 
      aux2 = self.head      
      while aux2:
        aux2 = aux2.get_next()
        if aux2:
          aux2 = aux2.get_next()
          aux = aux.get_next()
      aux2 = self.head
      
      while aux.get_next():          
        temp = aux.get_next()        
        aux.set_next(aux2.get_next()) 
        aux2.set_next(aux)
        aux2 = aux.get_next()
        aux = temp
      aux2.set_next(aux)

a = int(input())
b = int(input())
lista = LinkedList(b)
for i in range(a-1):
    c = int(input())
    lista.append(c)
lista.inter_med()
lista.print_list()

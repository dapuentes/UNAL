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
    
    def find(self, value):
        aux = self.head
        cont = 0 
        index = None
        while aux:
            if aux.value == value:
                index = cont
                break
            else:
                aux = aux.get_next()
                cont += 1
        return index
    
    def nodo_sig(self, value):
      aux = self.head
      temp = True
      while aux:
        if aux.get_value()== value:
          print(aux.get_next().get_value())
          temp=False
        aux = aux.get_next()
      if temp:
        print("no se encuentra")

    def nodos_ant(self, value):
      pre = self.head
      aux = self.head
      temp = True
      while aux.get_next():
        aux = aux.get_next()
        if aux.get_value()==value:
          print(pre.get_value())
          temp = False
        pre = aux
      if temp:
        print("no se encuentra")

                
a = int(input())
b = int(input())
lista = LinkedList(b)
for i in range(a-1):
    c = int(input())
    lista.append(c)
d = int(input())
if d % 2 == 0:
    lista.nodo_sig(d)
else:
    lista.nodos_ant(d)
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):        
        self.root = None

    def insert(self, value):
        node = Node(value)
        if self.root is None:
            self.root = node
            return True
        aux = self.root
        while True:
            if node.value == aux.value:
                return False
            if node.value < aux.value:
                if aux.left is None:
                    aux.left = node
                    return True
                aux = aux.left
            else:
                if aux.right is None:
                    aux.right = node
                    return True
                aux = aux.right

    def find(self, value):
        aux = self.root
        while aux:
            if value < aux.value:
                aux = aux.left
            elif value > aux.value:
                aux = aux.right
            else:
                return aux
        return None

    def find_ancestro(self, value):
        aux = self.root
        while aux.left or aux.right:
            if aux.left and aux.left.value == value:
                return aux
            elif aux.right and aux.right.value == value:
                return aux
            elif value < aux.value:
                aux = aux.left
            else:
                aux = aux.right
        return None

    def ancestro_comun(self, value1, value2):
        node1 = self.find(value1)
        node2 = self.find(value2)
        if node1 is None or node2 is None:
            return None
        ancestro1 = self.find_ancestro(value1)
        ancestro2 = self.find_ancestro(value2)
        while ancestro1 != ancestro2:
            if ancestro1 is None:
                ancestro1 = self.find_ancestro(value2)
            else:
                ancestro1 = self.find_ancestro(ancestro1.value)
            if ancestro2 is None:
                ancestro2 = self.find_ancestro(value1)
            else:
                ancestro2 = self.find_ancestro(ancestro2.value)
        if ancestro1 is None:
            return None
        print("el menor ancestro comun es", ancestro1.value)
        

 
    def dfs_in_order(self):
        results = []
        def traverse(node):
            if node.left is not None:
                traverse(node.left)
            results.append(node.value) 
            if node.right is not None:
                traverse(node.right)          
        traverse(self.root)
        return results
    
arbol = BinaryTree()
a = int(input())
for i in range(a):
    b = int(input())
    arbol.insert(b)

c = int(input())
d = int(input())

arbol.ancestro_comun(c, d)

e = arbol.dfs_in_order()
f = " ".join(map(str, e))
print(f)

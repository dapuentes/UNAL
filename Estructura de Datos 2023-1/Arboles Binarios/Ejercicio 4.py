class Node:
    def __init__(self, value, value1):
        self.value = value
        self.value1 = value1
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def __init__(self):        
        self.root = None

    def insert(self, node, value, value1):
        if self.root is None:
            node = Node(value, value1)
            self.root = node
            return node

        if not node:
            return Node(value, value1)

        if value < node.value:
            node.left = self.insert(node.left, value, value1)
        elif value > node.value:
            node.right = self.insert(node.right, value, value1)
        else:
            return None
        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))

        balance = self.get_balance(node)
        if balance > 1 and value < node.left.value:
            return self.rotate_right(node)

        if balance < -1 and value > node.right.value:
            return self.rotate_left(node)

        if balance > 1 and value > node.left.value:
            node.left = self.rotate_left(node.left)
            return self.rotate_right(node)

        if balance < -1 and value < node.right.value:
            node.right = self.rotate_right(node.right)
            return self.rotate_left(node)
        return node

    def get_height(self, node):
        if not node:
            return 0
        return node.height

    def get_balance(self, node):
        if not node:
            return 0
        return self.get_height(node.left)-self.get_height(node.right)

    def rotate_left(self, node):
        new_root = node.right
        node.right = new_root.left
        new_root.left = node
        if node == self.root:
            self.root = new_root
        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
        new_root.height = 1 + max(self.get_height(new_root.left), self.get_height(new_root.right))
        return new_root

    def rotate_right(self, node):
        new_root = node.left
        node.left = new_root.right
        new_root.right = node
        if node == self.root:
            self.root = new_root
        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
        new_root.height = 1 + max(self.get_height(new_root.left), self.get_height(new_root.right))
        return new_root  
        
    def find_successor(self, node):
        while node.left:
            node = node.left        
        return node
                
    def in_order(self):
        results = []
        def traverse(node):            
            if node.left is not None:
                traverse(node.left)
            results.append([node.value, node.height])
            if node.right is not None:
                traverse(node.right)
        traverse(self.root)
        return results

    def buscar(self, value):
        node = self.root
        aux = 0
        while node:
            if value < node.value:
                node = node.left
            elif value > node.value:
                node = node.right
            else:
                print(node.value1)
                print("encontrada en", aux, "pasos")
                return True
            aux += 1
        print("palabra no encontrada")
        return False
            
            
                

arbol = AVLTree()
a = int(input())
for i in range(a):
    b, f = input().split(" - ")
    arbol.root = arbol.insert(arbol.root, b, f)

c = int(input())
for i in range(c):
    d = input()
    arbol.buscar(d)

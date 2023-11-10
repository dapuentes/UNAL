class Node:
    def __init__(self, name, value):
        self.name = name
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, value):
        node = Node(None, value)
        self.root = node

    def insert(self, name, value):
        node = Node(name, value)
        if self.root is None:
            self.root = node
            return True
        aux = self.root
        while True:
            if value == aux.value:
                if aux.right is None:
                    aux.right = node
                    return True
                aux = aux.right
            elif value < aux.value:
                if aux.left is None:
                    aux.left = node
                    return True
                aux = aux.left
            else:
                if aux.right is None:
                    aux.right = node
                    return True
                aux = aux.right

    def nota_estudiante(self):
        results = []
        def traverse(node):
            if node.left is not None:
                traverse(node.left)
            if node != self.root:                
                results.append([node.value,node.name]) 
            if node.right is not None:
                traverse(node.right)          
        traverse(self.root)
        return results

    def dfs_pre_order(self):
        def traverse(node):
            if node is None:
                return []
            left = traverse(node.left)
            right = traverse(node.right)
            return [(node.name, node.value)] + left + right

        result = traverse(self.root)
        if len(result) > 0:
            result = result[1:]
        return result
    
a = int(input())
arbol = BinaryTree(3)
for i in range(a):
    b = input()
    c, d = b.split(":")
    arbol.insert(c, float(d))
e = int(input())

estudiante = arbol.nota_estudiante()[e-1]
print(f"{estudiante[1]} con nota de {estudiante[0]}")
students = arbol.dfs_pre_order()
f = " ".join([student[0] for student in students])
print(f)
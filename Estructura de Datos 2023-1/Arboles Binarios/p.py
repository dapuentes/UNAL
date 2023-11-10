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
        return False

    
    def find_parent(self, value):
        aux = self.root
        while aux.left or aux.right:
            if aux.left and aux.left.value == value:
                return aux
            elif aux.right and aux.right.value == value:
                return aux
            elif value < aux.value:
                aux = aux.left
            else :
                aux = aux.right
        return False

    def find_successor(self, node):
        while node.left:
            node = node.left
        value = node.value
        self.delete(value)
        return value  

    def delete(self, value):
        print(value)
        aux = self.find(value)
        if aux is None:
            return False

        #Caso 1 - sin hijos
        if not aux.left and not aux.right:
            if aux == self.root:
                self.root = None
            else:
                parent = self.find_parent(value)
                if aux == parent.left:
                    parent.left = None
                else:                                      
                    parent.right = None
                

        #Caso 2 - un solo hijo
        #hijo derecho
        elif not aux.left:
            if aux == self.root:
                self.root = aux.right
            else:
                parent = self.find_parent(value)
                if aux == parent.left:
                    parent.left = aux.right
                else :
                    parent.right = aux.right
                    
                
        #hijo izquierdo
        elif not aux.right:
            if aux == self.root:
                self.root = aux.left
            else:
                parent = self.find_parent(value)
                if aux == parent.left:
                    parent.left = aux.left
                else :
                    parent.right = aux.left
                    
        #Caso 3 - dos hijos
        else:
            suc = self.find_successor(aux.right)
            aux.value = suc
        return True

    def BFS(self):
        node = self.root
        queue = []
        results = []
        queue.append(node)
        while len(queue) > 0:
            node = queue.pop(0)            
            results.append(node.value)
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
        return results
    

    def dfs_pre_order(self):
        results = []
        def traverse(node):
            results.append(node.value)
            if node.left is not None:
                traverse(node.left)
            if node.right is not None:
                traverse(node.right)
        traverse(self.root)
        return results

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

    def dfs_post_order(self):
        results = []
        def traverse(node):
            if node.left is not None:
                traverse(node.left)
            if node.right is not None:
                traverse(node.right)
            results.append(node.value)
        traverse(self.root)
        return results
    
    def find_pairs(self, target):
        pairs = []
        stack = []
        stack.append(self.root)
        while stack:
            node = stack.pop()
            if node.left:
                diff = node.left.value - node.value
                if diff == target:
                    pairs.append((node.left.value, node.value))
                stack.append(node.left)
            if node.right:
                diff = node.right.value - node.value
                if diff == target:
                    pairs.append((node.right.value, node.value))
                stack.append(node.right)
        return pairs

    def print_pairs(self, target):
        pairs = self.find_pairs(target)
        for pair in pairs:
            print(f"{pair[0]} {pair[1]}")

# Crear el árbol de búsqueda binaria
binary_tree = BinaryTree()
elements = [10, 4, 12, 14, 2, 8, 17, 16, 1, 6, 2]
for element in elements:
    binary_tree.insert(element)

# Buscar parejas con diferencia 2 e imprimir
target = 2
binary_tree.print_pairs(target)
